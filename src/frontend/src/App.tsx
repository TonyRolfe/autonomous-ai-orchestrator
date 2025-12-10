import React from 'react';
import ChatInterface from './components/ChatInterface';
import NavBar from './components/NavBar';

/**
 * Root application component – FINAL VERSION.
 * Will never be modified again in this Epic (or likely ever).
 */
function App(): React.JSX.Element {
  return (
    <div className="relative flex h-screen flex-col bg-gray-900">
      {/* 1. NavBar – sits on top (z-10), hidden by default */}
      <NavBar />

      {/* 2. ChatInterface – takes remaining space, handles its OWN scrolling */}
      <div className="flex-1">
        <ChatInterface />
      </div>
    </div>
  );
}

export default App;