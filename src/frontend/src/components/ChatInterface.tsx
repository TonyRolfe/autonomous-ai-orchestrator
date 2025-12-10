import React, { useState, useRef, useEffect } from 'react';
import MessageBubble from './MessageBubble';

interface Message {
  id: string;
  text: string;
  sender: 'user' | 'ai';
}

/**
 * Full-screen chat interface.
 * Uses MessageBubble component for all messages.
 * Mobile-safe, auto-scrolls, Enter to send.
 */
const ChatInterface: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      text: 'Hello! I’m your Autonomous AI Orchestrator. Describe the Epic you want to create, and I’ll generate everything automatically.',
      sender: 'ai',
    },
  ]);
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSend = () => {
  if (!input.trim()) return;

  const userMsg: Message = {
    id: Date.now().toString(),
    text: input,
    sender: 'user',
  };
  setMessages((prev) => [...prev, userMsg]);
  setInput('');

  setMessages((prev) => [
    ...prev,
    {
      id: (Date.now() + 1).toString(),
      text: 'Your Agentic AI Team is working on your request. Please wait...',
      sender: 'ai',
    },
  ]);
};

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div className="flex h-full flex-col bg-gray-900">
      {/* Message List */}
      <div className="flex-1 overflow-y-auto px-4 pt-20 pb-4 scrollbar-thin">
        <div className="mx-auto max-w-4xl space-y-4">
          {messages.map((msg) => (
            <MessageBubble key={msg.id} text={msg.text} sender={msg.sender} />
          ))}
          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Input Bar */}
      <div className="border-t border-gray-700 bg-gray-950 px-4 pb-safe-bottom pt-4">
        <div className="mx-auto max-w-4xl">
          <div className="flex gap-4">
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Describe your Epic in natural language..."
              className="
                flex-1 resize-none rounded-2xl bg-gray-900 px-6 py-5
                text-lg text-gray-100 placeholder-gray-500
                outline-none ring-2 ring-transparent
                focus:ring-blue-500 transition-all
                scrollbar-thin scrollbar-thumb-gray-700
              "
              rows={2}
              style={{ minHeight: '64px' }}
            />
            <button
              onClick={handleSend}
              disabled={!input.trim()}
              className="
                rounded-2xl bg-blue-600 px-8 py-5 font-semibold text-white
                transition-all hover:bg-blue-500 active:scale-95
                disabled:opacity-40 disabled:hover:bg-blue-600
                disabled:cursor-not-allowed flex items-center gap-2
              "
            >
              <span>Send</span>
              <svg className="h-5 w-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" />
              </svg>
            </button>
          </div>
          <p className="mt-3 text-center text-xs text-gray-500">
            Press Enter to send • Shift+Enter for new line
          </p>
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;