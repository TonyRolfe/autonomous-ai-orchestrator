// src/components/MessageBubble.tsx
import React from 'react';

interface MessageBubbleProps {
  text: string;
  sender: 'user' | 'ai';
}

/**
 * Reusable message bubble – fully typed, accessible, and testable.
 */
const MessageBubble: React.FC<MessageBubbleProps> = ({ text, sender }) => {
  return (
    <div className={`flex ${sender === 'user' ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`
          max-w-lg rounded-2xl px-4 py-3 text-sm md:text-base
          ${sender === 'user'
            ? 'bg-blue-600 text-white'
            : 'bg-gray-800 text-gray-100 border border-gray-700'
          }
        `}
      >
        {text}
      </div>
    </div>
  );
};

export default MessageBubble;