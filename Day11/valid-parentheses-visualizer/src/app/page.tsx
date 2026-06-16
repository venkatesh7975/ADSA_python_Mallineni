"use client";

import { useState, useEffect, useRef } from "react";
import { Play, Pause, RotateCcw, SkipForward, SkipBack, Shuffle } from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { simulateValidParentheses, Step, SimulationResult } from "@/lib/simulator";
import { cn } from "@/lib/utils";

// Example cases for random button
const EXAMPLES = ["()", "()[]{}", "([{}])", "(]", "([)]", "((()))", "{[()]}", "]", "((", ""];

export default function Visualizer() {
  const [inputStr, setInputStr] = useState("([{}])");
  const [simulation, setSimulation] = useState<SimulationResult | null>(null);
  const [stepIndex, setStepIndex] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);
  const [speedMs, setSpeedMs] = useState(1000);
  const [learningMode, setLearningMode] = useState(true);

  // Initialize simulation when input changes
  useEffect(() => {
    const res = simulateValidParentheses(inputStr);
    setSimulation(res);
    setStepIndex(0);
    setIsPlaying(false);
  }, [inputStr]);

  // Playback timer
  useEffect(() => {
    if (!isPlaying || !simulation) return;

    if (stepIndex >= simulation.steps.length - 1) {
      setIsPlaying(false);
      return;
    }

    const timer = setTimeout(() => {
      setStepIndex((prev) => prev + 1);
    }, speedMs);

    return () => clearTimeout(timer);
  }, [isPlaying, stepIndex, simulation, speedMs]);

  if (!simulation) return null;

  const currentStep = simulation.steps[stepIndex] || simulation.steps[0];
  const isDone = stepIndex === simulation.steps.length - 1;

  const handleRandom = () => {
    const randomExample = EXAMPLES[Math.floor(Math.random() * EXAMPLES.length)];
    setInputStr(randomExample);
  };

  return (
    <div className="min-h-screen bg-neutral-950 text-neutral-100 font-sans p-4 md:p-8 selection:bg-indigo-500/30">
      
      {/* HEADER & HERO */}
      <header className="max-w-6xl mx-auto flex flex-col items-center justify-center py-10 space-y-4">
        <div className="absolute top-0 left-0 w-full h-[500px] bg-gradient-to-br from-indigo-500/10 via-purple-500/10 to-transparent blur-3xl -z-10" />
        <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-indigo-400 to-purple-400">
          Valid Parentheses Visualizer
        </h1>
        <p className="text-lg text-neutral-400 text-center max-w-2xl">
          Learn the Stack Data Structure through interactive execution.
        </p>

        {/* INPUT AND CONTROLS */}
        <div className="w-full max-w-3xl mt-8 p-6 bg-neutral-900/50 backdrop-blur-xl border border-neutral-800 rounded-2xl shadow-2xl flex flex-col space-y-6">
          <div className="flex flex-col md:flex-row gap-4 items-center">
            <input
              type="text"
              value={inputStr}
              onChange={(e) => setInputStr(e.target.value)}
              placeholder="Enter parentheses..."
              className="flex-1 w-full bg-neutral-950 border border-neutral-800 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition-all font-mono text-lg"
            />
            <button
              onClick={handleRandom}
              className="px-4 py-3 bg-neutral-800 hover:bg-neutral-700 rounded-xl transition-colors flex items-center gap-2 font-medium"
            >
              <Shuffle className="w-4 h-4" /> Random
            </button>
          </div>

          <div className="flex flex-wrap items-center justify-between gap-4">
            <div className="flex items-center gap-2">
              <button
                onClick={() => setStepIndex(0)}
                className="p-3 bg-neutral-800 hover:bg-neutral-700 rounded-lg transition-colors"
                title="Reset"
              >
                <RotateCcw className="w-5 h-5" />
              </button>
              <button
                onClick={() => setStepIndex(Math.max(0, stepIndex - 1))}
                className="p-3 bg-neutral-800 hover:bg-neutral-700 rounded-lg transition-colors"
                disabled={stepIndex === 0}
              >
                <SkipBack className="w-5 h-5" />
              </button>
              <button
                onClick={() => setIsPlaying(!isPlaying)}
                className={cn(
                  "p-3 rounded-lg transition-colors w-12 flex justify-center items-center",
                  isPlaying ? "bg-red-500/20 text-red-400 hover:bg-red-500/30" : "bg-indigo-500 hover:bg-indigo-600 text-white"
                )}
              >
                {isPlaying ? <Pause className="w-5 h-5 fill-current" /> : <Play className="w-5 h-5 fill-current" />}
              </button>
              <button
                onClick={() => setStepIndex(Math.min(simulation.steps.length - 1, stepIndex + 1))}
                className="p-3 bg-neutral-800 hover:bg-neutral-700 rounded-lg transition-colors"
                disabled={isDone}
              >
                <SkipForward className="w-5 h-5" />
              </button>
            </div>

            <div className="flex items-center gap-4">
              <div className="flex items-center gap-2 text-sm text-neutral-400">
                <label>Speed:</label>
                <select
                  value={speedMs}
                  onChange={(e) => setSpeedMs(Number(e.target.value))}
                  className="bg-neutral-950 border border-neutral-800 rounded px-2 py-1 outline-none focus:ring-1 focus:ring-indigo-500"
                >
                  <option value={2000}>0.5x</option>
                  <option value={1000}>1.0x</option>
                  <option value={500}>2.0x</option>
                  <option value={200}>Fast</option>
                </select>
              </div>
              <label className="flex items-center gap-2 text-sm cursor-pointer select-none">
                <input
                  type="checkbox"
                  checked={learningMode}
                  onChange={(e) => setLearningMode(e.target.checked)}
                  className="rounded border-neutral-700 text-indigo-500 focus:ring-indigo-500 bg-neutral-900"
                />
                Learning Mode
              </label>
            </div>
          </div>
        </div>
      </header>

      {/* MAIN VISUALIZATION AREA */}
      <main className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-8 my-8">
        
        {/* LEFT PANEL: String traversal & Learning Box */}
        <div className="flex flex-col gap-6">
          <div className="p-6 bg-neutral-900/50 border border-neutral-800 rounded-2xl flex flex-col items-center justify-center min-h-[200px]">
            <h3 className="text-sm font-semibold text-neutral-500 uppercase tracking-wider mb-6">Input String</h3>
            <div className="flex flex-wrap justify-center gap-2 text-3xl font-mono">
              {inputStr.split('').map((char, idx) => {
                const isActive = idx === currentStep.charIndex;
                const isPast = idx < currentStep.charIndex;
                return (
                  <motion.div
                    key={idx}
                    animate={{
                      scale: isActive ? 1.2 : 1,
                      y: isActive ? -10 : 0,
                    }}
                    className={cn(
                      "w-12 h-14 flex items-center justify-center rounded-lg border-b-4 transition-colors",
                      isActive
                        ? "bg-indigo-500/20 text-indigo-300 border-indigo-500 shadow-[0_0_15px_rgba(99,102,241,0.5)]"
                        : isPast
                        ? "bg-neutral-800/50 text-neutral-500 border-neutral-700"
                        : "bg-neutral-800 text-neutral-200 border-neutral-600"
                    )}
                  >
                    {char}
                  </motion.div>
                );
              })}
              {inputStr.length === 0 && <span className="text-neutral-600 italic text-xl">Empty String</span>}
            </div>
          </div>

          {/* Learning Mode Output */}
          <AnimatePresence mode="wait">
            {learningMode && (
              <motion.div
                key={stepIndex}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -10 }}
                className={cn(
                  "p-6 border rounded-2xl",
                  currentStep.isError
                    ? "bg-red-500/10 border-red-500/30"
                    : isDone && simulation.isValid
                    ? "bg-emerald-500/10 border-emerald-500/30"
                    : "bg-neutral-900/50 border-neutral-800"
                )}
              >
                <h3 className="text-sm font-semibold text-neutral-500 uppercase tracking-wider mb-4">
                  Step {stepIndex} Explanation
                </h3>
                <div className="space-y-2 font-mono text-sm">
                  <p>
                    <span className="text-neutral-400">Action:</span>{" "}
                    <span className={cn(
                      currentStep.action === 'Push' ? 'text-blue-400' :
                      currentStep.action === 'Pop Compare' ? 'text-amber-400' :
                      currentStep.action === 'Error' ? 'text-red-400' : 'text-emerald-400'
                    )}>
                      {currentStep.action}
                    </span>
                  </p>
                  {currentStep.char && (
                    <p><span className="text-neutral-400">Character:</span> '{currentStep.char}'</p>
                  )}
                  {currentStep.expectedChar && (
                    <p><span className="text-neutral-400">Expected Top:</span> '{currentStep.expectedChar}'</p>
                  )}
                  <p className="mt-4 text-base leading-relaxed text-neutral-200">
                    {currentStep.message}
                  </p>
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>

        {/* RIGHT PANEL: Stack Visualization */}
        <div className="p-6 bg-neutral-900/50 border border-neutral-800 rounded-2xl flex flex-col items-center min-h-[400px]">
           <h3 className="text-sm font-semibold text-neutral-500 uppercase tracking-wider mb-8">Stack State</h3>
           
           <div className="w-40 flex-1 flex flex-col justify-end items-center relative border-b-4 border-l-4 border-r-4 border-neutral-700 rounded-b-xl pb-2 bg-neutral-950/50 shadow-inner">
             {/* Open Top Indicator */}
             <div className="absolute top-0 w-full h-10 bg-gradient-to-b from-neutral-900/0 to-neutral-950/0" />
             
             <div className="flex flex-col justify-end w-full px-2 gap-2 mt-10">
                <AnimatePresence initial={false}>
                  {currentStep.stackAfter.map((char, i) => (
                    <motion.div
                      key={`${i}-${char}`}
                      initial={{ opacity: 0, y: -50, scale: 0.8 }}
                      animate={{ opacity: 1, y: 0, scale: 1 }}
                      exit={{ opacity: 0, x: 50, scale: 0.8 }}
                      transition={{ type: "spring", stiffness: 300, damping: 20 }}
                      className={cn(
                        "w-full h-12 flex items-center justify-center text-2xl font-bold font-mono rounded-md shadow-lg",
                        "bg-indigo-500 text-white border-2 border-indigo-400"
                      )}
                    >
                      {char}
                    </motion.div>
                  ))}
                </AnimatePresence>
             </div>
             
             {currentStep.stackAfter.length === 0 && (
               <div className="absolute inset-0 flex items-center justify-center text-neutral-600 font-mono italic">
                 Empty
               </div>
             )}
           </div>
        </div>

      </main>

      {/* RESULT OVERLAY IF DONE */}
      <AnimatePresence>
        {isDone && (
           <motion.div
             initial={{ opacity: 0, scale: 0.9 }}
             animate={{ opacity: 1, scale: 1 }}
             exit={{ opacity: 0 }}
             className="max-w-6xl mx-auto my-8 p-8 rounded-2xl flex flex-col items-center justify-center text-center shadow-2xl"
             style={{
               backgroundColor: simulation.isValid ? 'rgba(16, 185, 129, 0.1)' : 'rgba(239, 68, 68, 0.1)',
               border: `1px solid ${simulation.isValid ? 'rgba(16, 185, 129, 0.3)' : 'rgba(239, 68, 68, 0.3)'}`
             }}
           >
              <div className={cn(
                "w-20 h-20 rounded-full flex items-center justify-center mb-4 text-4xl",
                simulation.isValid ? "bg-emerald-500/20 text-emerald-400" : "bg-red-500/20 text-red-400"
              )}>
                {simulation.isValid ? "✓" : "✗"}
              </div>
              <h2 className="text-3xl font-bold mb-2">
                {simulation.isValid ? "Valid Parentheses" : "Invalid Parentheses"}
              </h2>
              <p className="text-neutral-400">
                {simulation.isValid 
                  ? "All brackets matched perfectly and the stack is empty." 
                  : "A mismatch or leftover bracket was detected."}
              </p>
           </motion.div>
        )}
      </AnimatePresence>

      {/* DRY RUN TABLE */}
      <section className="max-w-6xl mx-auto my-16">
        <h2 className="text-2xl font-bold mb-6">Dry Run Execution Table</h2>
        <div className="overflow-x-auto rounded-xl border border-neutral-800 shadow-xl bg-neutral-900/50">
          <table className="w-full text-left text-sm whitespace-nowrap">
            <thead className="bg-neutral-900 text-neutral-400 uppercase tracking-wider text-xs">
              <tr>
                <th className="px-6 py-4">Step</th>
                <th className="px-6 py-4">Character</th>
                <th className="px-6 py-4">Action</th>
                <th className="px-6 py-4">Stack Before</th>
                <th className="px-6 py-4">Stack After</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-neutral-800">
              {simulation.steps.map((step) => {
                if (step.stepIndex === 0) return null; // Skip initial empty state if any
                const isActive = step.stepIndex === stepIndex;
                return (
                  <tr 
                    key={step.stepIndex} 
                    className={cn(
                      "transition-colors",
                      isActive ? "bg-indigo-500/10 text-indigo-200" : "hover:bg-neutral-800/50 text-neutral-300"
                    )}
                  >
                    <td className="px-6 py-4 font-mono">{step.stepIndex}</td>
                    <td className="px-6 py-4 font-mono text-lg">{step.char || '-'}</td>
                    <td className="px-6 py-4">
                      <span className={cn(
                        "px-2 py-1 rounded text-xs font-semibold",
                        step.action === 'Push' ? "bg-blue-500/20 text-blue-400" :
                        step.action === 'Pop Compare' ? "bg-amber-500/20 text-amber-400" :
                        step.action === 'Error' ? "bg-red-500/20 text-red-400" : "bg-emerald-500/20 text-emerald-400"
                      )}>
                        {step.action}
                      </span>
                    </td>
                    <td className="px-6 py-4 font-mono">[{step.stackBefore.join(', ')}]</td>
                    <td className="px-6 py-4 font-mono">[{step.stackAfter.join(', ')}]</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </section>

      {/* THEORY SECTION */}
      <section className="max-w-6xl mx-auto my-16 grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="bg-neutral-900/50 p-8 rounded-2xl border border-neutral-800">
          <h2 className="text-2xl font-bold mb-4">Why use a Stack?</h2>
          <p className="text-neutral-300 leading-relaxed mb-4">
            The "Valid Parentheses" problem is the classic textbook example for the <strong>Stack</strong> data structure.
            Stacks follow the <strong>Last-In, First-Out (LIFO)</strong> principle.
          </p>
          <ul className="list-disc pl-5 space-y-2 text-neutral-400">
            <li>When we see an <strong>opening bracket</strong>, we don't yet know when it will be closed, so we push it onto the stack to remember it.</li>
            <li>When we see a <strong>closing bracket</strong>, it MUST match the most recently opened unclosed bracket.</li>
            <li>Because a Stack pops the <em>most recently pushed</em> item, it perfectly models this "most recently opened" requirement.</li>
          </ul>
        </div>

        <div className="bg-neutral-900/50 p-8 rounded-2xl border border-neutral-800">
          <h2 className="text-2xl font-bold mb-4">Complexity Analysis</h2>
          
          <div className="space-y-6">
            <div>
              <div className="flex justify-between items-end mb-2">
                <h4 className="font-semibold text-emerald-400">Time Complexity</h4>
                <span className="font-mono text-xl bg-neutral-800 px-2 py-1 rounded">O(n)</span>
              </div>
              <p className="text-sm text-neutral-400">
                We iterate through the string of length <span className="font-mono">n</span> exactly once. 
                Stack push and pop operations are <span className="font-mono">O(1)</span> time.
              </p>
              {/* Visual Graph line */}
              <div className="w-full bg-neutral-800 h-2 mt-4 rounded-full overflow-hidden">
                <div className="bg-emerald-500 h-full w-1/2 rounded-full" />
              </div>
            </div>

            <div>
              <div className="flex justify-between items-end mb-2">
                <h4 className="font-semibold text-blue-400">Space Complexity</h4>
                <span className="font-mono text-xl bg-neutral-800 px-2 py-1 rounded">O(n)</span>
              </div>
              <p className="text-sm text-neutral-400">
                In the worst-case scenario (e.g., all opening brackets <span className="font-mono">"((((("</span>), we will push every character onto the stack, requiring space proportional to <span className="font-mono">n</span>.
              </p>
               {/* Visual Graph line */}
               <div className="w-full bg-neutral-800 h-2 mt-4 rounded-full overflow-hidden">
                <div className="bg-blue-500 h-full w-1/2 rounded-full" />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CODE & TIPS SECTION */}
      <section className="max-w-6xl mx-auto my-16 bg-neutral-900/50 p-8 rounded-2xl border border-neutral-800">
        <div className="flex flex-col md:flex-row gap-8">
          <div className="flex-1">
             <h2 className="text-2xl font-bold mb-4">Python Solution</h2>
             <pre className="bg-neutral-950 p-4 rounded-xl border border-neutral-800 overflow-x-auto">
               <code className="text-sm font-mono text-neutral-300">
{`def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack.pop() != mapping[ch]:
                return False

    return len(stack) == 0`}
               </code>
             </pre>
          </div>
          <div className="flex-1">
            <h2 className="text-2xl font-bold mb-4">Interview Tips</h2>
            <div className="space-y-4">
              <div className="bg-amber-500/10 border border-amber-500/20 p-4 rounded-xl">
                <h4 className="text-amber-400 font-bold mb-2">Common Mistake #1</h4>
                <p className="text-sm text-neutral-300">Forgetting to check if the stack is empty before popping. If the string is <code>"]"</code>, calling <code>pop()</code> on an empty stack throws an error.</p>
              </div>
              <div className="bg-amber-500/10 border border-amber-500/20 p-4 rounded-xl">
                <h4 className="text-amber-400 font-bold mb-2">Common Mistake #2</h4>
                <p className="text-sm text-neutral-300">Forgetting to check if the stack is empty at the END. If the string is <code>"()"</code>, it matches, but if it is <code>"()("</code>, there's a leftover open bracket. Returning <code>True</code> immediately after the loop without checking <code>len(stack) == 0</code> is a failure.</p>
              </div>
              <div className="bg-indigo-500/10 border border-indigo-500/20 p-4 rounded-xl">
                <h4 className="text-indigo-400 font-bold mb-2">Pattern Recognition</h4>
                <p className="text-sm text-neutral-300">Whenever you see a problem involving "nested structures", "matching pairs", or "evaluating expressions", your brain should immediately think: <strong>STACK</strong>.</p>
              </div>
            </div>
          </div>
        </div>
      </section>

    </div>
  );
}
