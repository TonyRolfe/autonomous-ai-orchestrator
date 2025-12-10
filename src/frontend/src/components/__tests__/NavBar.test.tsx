// src/components/__tests__/NavBar.test.tsx
import { render, screen } from '@testing-library/react';
import NavBar from '../NavBar';

describe('NavBar', () => {
  it('renders hidden by default (translate-y-full)', () => {
    render(<NavBar />);
    const navbar = screen.getByRole('button', { name: /open history/i }).closest('div')!;
    expect(navbar).toHaveClass('-translate-y-full');
  });

  it('contains brand title', () => {
    render(<NavBar />);
    expect(screen.getByText('Autonomous AI Orchestrator')).toBeInTheDocument();
  });

  it('has mobile handle line', () => {
    render(<NavBar />);
    const handles = screen.getAllByRole('generic');
    const handleLine = handles.find(el =>
      el.classList.contains('pointer-coarse:block') &&
      el.classList.contains('h-1')
    );
    expect(handleLine).toBeInTheDocument();
  });
});