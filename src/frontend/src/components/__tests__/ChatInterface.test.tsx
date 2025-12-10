import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import ChatInterface from '../ChatInterface';

// jsdom doesn't have scrollIntoView — mock it globally
beforeAll(() => {
  window.HTMLElement.prototype.scrollIntoView = jest.fn();
});

describe('ChatInterface', () => {
  it('renders initial AI greeting', () => {
    render(<ChatInterface />);
    expect(screen.getByText(/Hello! I’m your Autonomous AI Orchestrator/i)).toBeInTheDocument();
  });

  it('sends message and shows working response', async () => {
    render(<ChatInterface />);
    const input = screen.getByPlaceholderText(/Describe your Epic/i);
    const sendButton = screen.getByRole('button', { name: /send/i });

    await userEvent.type(input, 'Create a login page');
    await userEvent.click(sendButton);

    expect(screen.getByText('Create a login page')).toBeInTheDocument();
    expect(screen.getByText(/Your Agentic AI Team is working on your request/i)).toBeInTheDocument();
  });

  it('sends message on Enter', async () => {
    render(<ChatInterface />);
    const input = screen.getByPlaceholderText(/Describe your Epic/i);

    await userEvent.type(input, 'Test{enter}');
    expect(screen.getByText('Test')).toBeInTheDocument();
    expect(screen.getByText(/Your Agentic AI Team is working/i)).toBeInTheDocument();
  });
});