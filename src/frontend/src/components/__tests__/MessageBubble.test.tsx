import { render, screen } from '@testing-library/react';
import MessageBubble from '../MessageBubble';

describe('MessageBubble', () => {
  it('renders user message with correct styling', () => {
    render(<MessageBubble text="Hello" sender="user" />);
    const bubble = screen.getByText('Hello');
    expect(bubble).toHaveClass('bg-blue-600', 'text-white');
    expect(bubble.parentElement).toHaveClass('justify-end');
  });

  it('renders AI message with correct styling', () => {
    render(<MessageBubble text="Hi there" sender="ai" />);
    const bubble = screen.getByText('Hi there');
    expect(bubble).toHaveClass('bg-gray-800', 'text-gray-100', 'border-gray-700');
    expect(bubble.parentElement).toHaveClass('justify-start');
  });
});