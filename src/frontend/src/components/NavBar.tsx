import React from 'react';

/**
 * NavBar – hidden by default, appears on hover (desktop) or tap on handle (mobile).
 * Contains future triggers for History (left) and User/Settings (right).
 * Never takes permanent space → fully compliant with US-01 "full-screen chat".
 */
const NavBar: React.FC = () => {
  return (
    <>
      {/* Thin handle line – visible on mobile/tablet, triggers reveal on tap */}
      <div className="pointer-coarse:block hidden h-1 w-full bg-gray-700/50" />

      {/* Main NavBar – slides down on hover (desktop) or tap (mobile) */}
      <div
        className={`
          absolute inset-x-0 top-0 z-10 flex h-16 items-center justify-between
          border-b border-gray-700 bg-gray-900/95 px-4 backdrop-blur-sm
          transition-all duration-300 ease-out
          /* Desktop: show on hover near top */
          hover:translate-y-0
          /* Mobile: show when handle tapped (via future state) */
          peer-hover:translate-y-0
          /* Default: hidden above viewport */
          -translate-y-full
          /* Override hide when mouse is near top (48px zone) */
          hover:[&]:translate-y-0
          /* Mobile handle acts as peer for hover-like behavior */
          peer-hover:[&]:translate-y-0
        `}
        // Desktop: detect mouse near top of viewport
        onMouseEnter={(e) => {
          if (window.innerWidth >= 1024) {
            e.currentTarget.style.transform = 'translateY(0)';
          }
        }}
      >
        {/* Left: Future History drawer trigger */}
        <button
          className="rounded-lg p-2 text-gray-400 hover:bg-gray-800 hover:text-gray-100 transition-colors"
          aria-label="Open history"
          disabled
        >
          <svg className="h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>

        {/* Center: Brand */}
        <div className="absolute left-1/2 -translate-x-1/2">
          <h1 className="text-lg font-semibold tracking-tight text-gray-100">
            Autonomous AI Orchestrator
          </h1>
        </div>

        {/* Right: Future User/Settings drawer trigger */}
        <button
          className="rounded-lg p-2 text-gray-400 hover:bg-gray-800 hover:text-gray-100 transition-colors"
          aria-label="Open user menu"
          disabled
        >
          <div className="h-8 w-8 rounded-full bg-gradient-to-br from-blue-500 to-purple-600" />
        </button>
      </div>
    </>
  );
};

export default NavBar;