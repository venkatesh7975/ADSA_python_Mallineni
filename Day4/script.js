const STEPS = [
  {
    type: "CALL",
    n: 4,
    depth: 1,
    line: 7, 
    explanation: "Program starts by calling factorial(4).",
    stack: [{n: 4, state: "running"}],
    tree: [{id: "f4", parent: null, n: 4, val: null, state: "running"}]
  },
  {
    type: "WAIT",
    n: 4,
    depth: 1,
    line: 5, 
    explanation: "factorial(4) cannot finish. It needs to know the result of factorial(3).",
    stack: [{n: 4, state: "waiting"}],
    tree: [{id: "f4", parent: null, n: 4, val: null, state: "waiting"}]
  },
  {
    type: "CALL",
    n: 3,
    depth: 2,
    line: 1, 
    explanation: "Now we are in factorial(3). n is 3. A new frame is pushed to the Call Stack.",
    stack: [{n: 4, state: "waiting"}, {n: 3, state: "running"}],
    tree: [
      {id: "f4", parent: null, n: 4, val: null, state: "waiting"},
      {id: "f3", parent: "f4", n: 3, val: null, state: "running"}
    ]
  },
  {
    type: "WAIT",
    n: 3,
    depth: 2,
    line: 5,
    explanation: "factorial(3) cannot finish. It needs factorial(2).",
    stack: [{n: 4, state: "waiting"}, {n: 3, state: "waiting"}],
    tree: [
      {id: "f4", parent: null, n: 4, val: null, state: "waiting"},
      {id: "f3", parent: "f4", n: 3, val: null, state: "waiting"}
    ]
  },
  {
    type: "CALL",
    n: 2,
    depth: 3,
    line: 1,
    explanation: "Now we are in factorial(2). n is 2.",
    stack: [{n: 4, state: "waiting"}, {n: 3, state: "waiting"}, {n: 2, state: "running"}],
    tree: [
      {id: "f4", parent: null, n: 4, val: null, state: "waiting"},
      {id: "f3", parent: "f4", n: 3, val: null, state: "waiting"},
      {id: "f2", parent: "f3", n: 2, val: null, state: "running"}
    ]
  },
  {
    type: "WAIT",
    n: 2,
    depth: 3,
    line: 5,
    explanation: "factorial(2) cannot finish. It needs factorial(1).",
    stack: [{n: 4, state: "waiting"}, {n: 3, state: "waiting"}, {n: 2, state: "waiting"}],
    tree: [
      {id: "f4", parent: null, n: 4, val: null, state: "waiting"},
      {id: "f3", parent: "f4", n: 3, val: null, state: "waiting"},
      {id: "f2", parent: "f3", n: 2, val: null, state: "waiting"}
    ]
  },
  {
    type: "CALL",
    n: 1,
    depth: 4,
    line: 1,
    explanation: "Now we are in factorial(1). n is 1.",
    stack: [{n: 4, state: "waiting"}, {n: 3, state: "waiting"}, {n: 2, state: "waiting"}, {n: 1, state: "running"}],
    tree: [
      {id: "f4", parent: null, n: 4, val: null, state: "waiting"},
      {id: "f3", parent: "f4", n: 3, val: null, state: "waiting"},
      {id: "f2", parent: "f3", n: 2, val: null, state: "waiting"},
      {id: "f1", parent: "f2", n: 1, val: null, state: "running"}
    ]
  },
  {
    type: "BASE",
    n: 1,
    depth: 4,
    line: 3,
    explanation: "BASE CASE REACHED! n is 1, so it returns 1. No more recursive calls are made.",
    stack: [{n: 4, state: "waiting"}, {n: 3, state: "waiting"}, {n: 2, state: "waiting"}, {n: 1, state: "base", val: 1}],
    tree: [
      {id: "f4", parent: null, n: 4, val: null, state: "waiting"},
      {id: "f3", parent: "f4", n: 3, val: null, state: "waiting"},
      {id: "f2", parent: "f3", n: 2, val: null, state: "waiting"},
      {id: "f1", parent: "f2", n: 1, val: 1, state: "base"}
    ],
    bubble: {from: "f1", to: "f2", val: 1}
  },
  {
    type: "RETURN",
    n: 2,
    depth: 3,
    line: 5,
    explanation: "factorial(1) popped from the stack! It returned 1. Now factorial(2) can compute 2 * 1 = 2.",
    stack: [{n: 4, state: "waiting"}, {n: 3, state: "waiting"}, {n: 2, state: "returned", val: 2}],
    tree: [
      {id: "f4", parent: null, n: 4, val: null, state: "waiting"},
      {id: "f3", parent: "f4", n: 3, val: null, state: "waiting"},
      {id: "f2", parent: "f3", n: 2, val: 2, state: "returned"},
      {id: "f1", parent: "f2", n: 1, val: 1, state: "returned"}
    ],
    bubble: {from: "f2", to: "f3", val: 2}
  },
  {
    type: "RETURN",
    n: 3,
    depth: 2,
    line: 5,
    explanation: "factorial(2) popped! It returned 2. Now factorial(3) can compute 3 * 2 = 6.",
    stack: [{n: 4, state: "waiting"}, {n: 3, state: "returned", val: 6}],
    tree: [
      {id: "f4", parent: null, n: 4, val: null, state: "waiting"},
      {id: "f3", parent: "f4", n: 3, val: 6, state: "returned"},
      {id: "f2", parent: "f3", n: 2, val: 2, state: "returned"},
      {id: "f1", parent: "f2", n: 1, val: 1, state: "returned"}
    ],
    bubble: {from: "f3", to: "f4", val: 6}
  },
  {
    type: "RETURN",
    n: 4,
    depth: 1,
    line: 5,
    explanation: "factorial(3) popped! It returned 6. Now factorial(4) can compute 4 * 6 = 24.",
    stack: [{n: 4, state: "returned", val: 24}],
    tree: [
      {id: "f4", parent: null, n: 4, val: 24, state: "returned"},
      {id: "f3", parent: "f4", n: 3, val: 6, state: "returned"},
      {id: "f2", parent: "f3", n: 2, val: 2, state: "returned"},
      {id: "f1", parent: "f2", n: 1, val: 1, state: "returned"}
    ],
    bubble: {from: "f4", to: "ROOT", val: 24}
  },
  {
    type: "DONE",
    n: 4,
    depth: 0,
    line: 7,
    explanation: "Recursion completed! The stack is empty. The final result is 24.",
    stack: [],
    tree: [
      {id: "f4", parent: null, n: 4, val: 24, state: "returned"},
      {id: "f3", parent: "f4", n: 3, val: 6, state: "returned"},
      {id: "f2", parent: "f3", n: 2, val: 2, state: "returned"},
      {id: "f1", parent: "f2", n: 1, val: 1, state: "returned"}
    ]
  }
];

// STATE variables
let currentStepIndex = 0;
let autoPlayInterval = null;

// DOM Elements
const btnPrev = document.getElementById('btn-prev');
const btnNext = document.getElementById('btn-next');
const btnPlay = document.getElementById('btn-play');
const btnRestart = document.getElementById('btn-restart');
const slider = document.getElementById('timeline-slider');

function init() {
    renderStep(currentStepIndex);
    
    btnPrev.addEventListener('click', () => {
        if (currentStepIndex > 0) {
            currentStepIndex--;
            renderStep(currentStepIndex);
        }
    });
    
    btnNext.addEventListener('click', () => {
        if (currentStepIndex < STEPS.length - 1) {
            currentStepIndex++;
            renderStep(currentStepIndex, true); // true indicates forward direction for animations
        }
    });
    
    slider.addEventListener('input', (e) => {
        currentStepIndex = parseInt(e.target.value, 10);
        renderStep(currentStepIndex);
    });
    
    btnRestart.addEventListener('click', () => {
        currentStepIndex = 0;
        if(autoPlayInterval) toggleAutoPlay();
        renderStep(currentStepIndex);
    });
    
    btnPlay.addEventListener('click', toggleAutoPlay);
}

function toggleAutoPlay() {
    const iconPlay = document.getElementById('icon-play');
    const iconPause = document.getElementById('icon-pause');
    const playText = document.getElementById('play-text');
    
    if (autoPlayInterval) {
        clearInterval(autoPlayInterval);
        autoPlayInterval = null;
        iconPlay.classList.remove('hidden');
        iconPlay.classList.add('block');
        iconPause.classList.add('hidden');
        iconPause.classList.remove('block');
        playText.textContent = 'Auto Play';
    } else {
        iconPlay.classList.add('hidden');
        iconPlay.classList.remove('block');
        iconPause.classList.remove('hidden');
        iconPause.classList.add('block');
        playText.textContent = 'Pause';
        
        if (currentStepIndex === STEPS.length - 1) {
            currentStepIndex = 0;
            renderStep(0);
        }
        
        autoPlayInterval = setInterval(() => {
            if (currentStepIndex < STEPS.length - 1) {
                currentStepIndex++;
                renderStep(currentStepIndex, true);
            } else {
                toggleAutoPlay(); // pause at end
            }
        }, 2000);
    }
}

function renderStep(index, isForward = false) {
    const step = STEPS[index];
    
    // Update UI controls
    slider.value = index;
    document.getElementById('current-step-label').textContent = index + 1;
    btnPrev.disabled = index === 0;
    btnNext.disabled = index === STEPS.length - 1;
    
    // Stats
    document.getElementById('stat-current-depth').textContent = step.depth;
    
    // Highlight Line
    highlightLine(step.line);
    
    // Explanation text
    document.getElementById('explanation-text').textContent = step.explanation;
    
    // Render components
    renderTree(step.tree, isForward ? step.bubble : null);
    renderStack(step.stack);
    renderVariables(step.stack);
}

function highlightLine(lineNumber) {
    const lineEl = document.getElementById(`line-${lineNumber}`);
    const highlight = document.getElementById('code-highlight');
    if (!lineEl || !highlight) return;
    
    // Calculate relative to the code-block parent
    const lineTop = lineEl.offsetTop;
    const lineHeight = lineEl.offsetHeight;
    
    highlight.style.top = `${lineTop}px`;
    highlight.style.height = `${lineHeight}px`;
    highlight.classList.remove('hidden');
}

function renderTree(treeData, bubbleData) {
    const container = document.getElementById('tree-container');
    container.innerHTML = '';
    
    const wrapper = document.createElement('div');
    wrapper.className = 'flex flex-col items-center w-full justify-start pt-2 pb-16 relative';
    
    treeData.forEach((node, index) => {
        // Connector before node (if not first)
        if (index > 0) {
            const line = document.createElement('div');
            let lineClass = 'w-0.5 h-8 transition-colors duration-500';
            if (node.state === 'returned' || node.state === 'base') {
                lineClass += ' bg-emerald-500 shadow-[0_0_10px_#10b981]';
            } else if (node.state === 'running') {
                lineClass += ' bg-blue-500 shadow-[0_0_10px_#3b82f6]';
            } else {
                lineClass += ' bg-gray-600';
            }
            line.className = lineClass;
            wrapper.appendChild(line);
        }
        
        // Node
        const nodeEl = document.createElement('div');
        nodeEl.id = `tree-node-${node.id}`;
        
        let stateClass = '';
        let iconHtml = '';
        
        if (node.state === 'running') {
            stateClass = 'tree-node-running text-blue-300 border-blue-500 bg-gray-800';
            iconHtml = `<div class="absolute -right-2 -top-2 bg-blue-500 w-4 h-4 rounded-full animate-ping"></div>`;
        } else if (node.state === 'waiting') {
            stateClass = 'tree-node-waiting text-gray-400 border-gray-600 bg-gray-800/50';
        } else if (node.state === 'base') {
            stateClass = 'tree-node-base text-amber-300 border-amber-400 font-bold';
        } else if (node.state === 'returned') {
            stateClass = 'tree-node-returned text-emerald-300 border-emerald-500 font-bold';
        }
        
        nodeEl.className = `tree-node border-2 rounded-xl px-5 py-3 flex flex-col items-center justify-center min-w-[160px] relative z-10 ${stateClass}`;
        
        let valStr = '';
        if (node.state === 'base' || node.state === 'returned') {
            valStr = `<div class="text-sm font-bold mt-2 px-2 py-0.5 rounded ${node.state === 'base' ? 'bg-amber-500/20 text-amber-200' : 'bg-emerald-500/20 text-emerald-200'}">Return: ${node.val}</div>`;
        }
        
        nodeEl.innerHTML = `
            ${iconHtml}
            <div class="font-mono text-base mb-1">factorial(${node.n})</div>
            <div class="text-xs opacity-70 font-mono text-purple-300">n = ${node.n}</div>
            ${valStr}
        `;
        
        wrapper.appendChild(nodeEl);
    });
    
    container.appendChild(wrapper);
    
    // Handle Bubble animation
    if (bubbleData) {
        setTimeout(() => triggerBubble(bubbleData, container), 100);
    }
}

function triggerBubble(bubbleData, container) {
    let startNodeId = `tree-node-${bubbleData.from}`;
    const startNode = document.getElementById(startNodeId);
    if (!startNode) return;
    
    const bubble = document.createElement('div');
    bubble.className = 'return-bubble';
    bubble.textContent = bubbleData.val;
    
    // Position relatively to the container
    const startRect = startNode.getBoundingClientRect();
    const containerRect = container.getBoundingClientRect();
    
    bubble.style.left = `${startRect.left - containerRect.left + (startRect.width / 2)}px`;
    bubble.style.top = `${startRect.top - containerRect.top}px`;
    
    container.appendChild(bubble);
    
    setTimeout(() => {
        if (container.contains(bubble)) {
            bubble.remove();
        }
    }, 1200);
}

function renderStack(stackData) {
    const container = document.getElementById('stack-container');
    container.innerHTML = '';
    
    if (stackData.length === 0) {
        const empty = document.createElement('div');
        empty.className = "text-gray-600 font-mono text-sm italic my-auto";
        empty.textContent = "Stack is empty";
        container.appendChild(empty);
        return;
    }
    
    stackData.forEach((frame) => {
        const frameEl = document.createElement('div');
        
        let bgClass = '';
        if (frame.state === 'running') {
            bgClass = 'bg-blue-900/40 border-blue-500 text-blue-200 shadow-[0_0_10px_rgba(59,130,246,0.3)]';
        } else if (frame.state === 'waiting') {
            bgClass = 'bg-gray-800/80 border-gray-600 text-gray-400';
        } else if (frame.state === 'base') {
            bgClass = 'bg-amber-900/40 border-amber-500 text-amber-200 shadow-[0_0_10px_rgba(245,158,11,0.3)]';
        } else if (frame.state === 'returned') {
            bgClass = 'bg-emerald-900/40 border-emerald-500 text-emerald-200 shadow-[0_0_10px_rgba(16,185,129,0.3)]';
        }
        
        frameEl.className = `stack-frame w-11/12 border-2 rounded-md p-2.5 text-center font-mono text-sm transition-all stack-frame-enter flex flex-col items-center ${bgClass}`;
        
        let html = `<div class="font-bold">factorial(${frame.n})</div>`;
        if (frame.val !== undefined) {
            html += `<div class="text-xs mt-1 px-2 py-0.5 rounded bg-black/30 text-emerald-300 border border-emerald-800">returned: ${frame.val}</div>`;
        }
        
        frameEl.innerHTML = html;
        container.appendChild(frameEl);
    });
}

function renderVariables(stackData) {
    const container = document.getElementById('variables-container');
    if (stackData.length === 0) {
        container.innerHTML = `<span class="text-gray-600 italic">No variables yet</span>`;
        return;
    }
    
    const topFrame = stackData[stackData.length - 1]; // Current top of stack
    
    let html = `<div class="flex items-center mb-1"><span class="text-purple-400 w-6">n</span> <span class="text-gray-500 mx-2">=</span> <span class="text-blue-300 font-bold text-lg">${topFrame.n}</span></div>`;
    
    if (topFrame.val !== undefined) {
        html += `<div class="flex items-center"><span class="text-purple-400 w-16">return</span> <span class="text-gray-500 mx-2">=</span> <span class="text-emerald-400 font-bold text-lg">${topFrame.val}</span></div>`;
    }
    
    container.innerHTML = html;
}

// Start app
window.addEventListener('DOMContentLoaded', init);
