export type StepAction = 'Push' | 'Pop Compare' | 'Error' | 'Done';

export interface Step {
  stepIndex: number;
  charIndex: number;
  char: string;
  action: StepAction;
  stackBefore: string[];
  stackAfter: string[];
  expectedChar?: string;
  isError: boolean;
  message: string;
}

export interface SimulationResult {
  steps: Step[];
  isValid: boolean;
}

export function simulateValidParentheses(s: string): SimulationResult {
  const steps: Step[] = [];
  const stack: string[] = [];
  const mapping: Record<string, string> = {
    ')': '(',
    ']': '[',
    '}': '{',
  };

  let stepIndex = 1;

  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    const stackBefore = [...stack];

    if (ch === '(' || ch === '[' || ch === '{') {
      stack.push(ch);
      steps.push({
        stepIndex: stepIndex++,
        charIndex: i,
        char: ch,
        action: 'Push',
        stackBefore,
        stackAfter: [...stack],
        isError: false,
        message: `Pushed '${ch}' to the stack.`,
      });
    } else {
      // It's a closing bracket
      if (stack.length === 0) {
        steps.push({
          stepIndex: stepIndex++,
          charIndex: i,
          char: ch,
          action: 'Error',
          stackBefore,
          stackAfter: [...stack],
          expectedChar: mapping[ch],
          isError: true,
          message: `Found '${ch}' but stack is empty! Expected an opening bracket.`,
        });
        return { steps, isValid: false };
      }

      const top = stack.pop()!;
      if (top !== mapping[ch]) {
        steps.push({
          stepIndex: stepIndex++,
          charIndex: i,
          char: ch,
          action: 'Error',
          stackBefore,
          stackAfter: [...stack],
          expectedChar: mapping[ch],
          isError: true,
          message: `Found '${ch}', expected closing for '${top}' but they do not match!`,
        });
        return { steps, isValid: false };
      }

      steps.push({
        stepIndex: stepIndex++,
        charIndex: i,
        char: ch,
        action: 'Pop Compare',
        stackBefore,
        stackAfter: [...stack],
        expectedChar: mapping[ch],
        isError: false,
        message: `Popped '${top}' from stack. Successfully matched with '${ch}'.`,
      });
    }
  }

  const isValid = stack.length === 0;

  steps.push({
    stepIndex: stepIndex++,
    charIndex: s.length, // Out of bounds means done
    char: '',
    action: 'Done',
    stackBefore: [...stack],
    stackAfter: [...stack],
    isError: !isValid,
    message: isValid
      ? 'All characters processed. Stack is empty. Valid parentheses!'
      : `All characters processed but stack is not empty (${stack.join(', ')}). Invalid parentheses!`,
  });

  return { steps, isValid };
}
