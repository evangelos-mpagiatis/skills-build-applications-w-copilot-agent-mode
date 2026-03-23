import { render, screen } from '@testing-library/react';
import App from './App';

test('renders OctoFit Tracker welcome heading', () => {
  render(<App />);
  const headingElement = screen.getByRole('heading', { name: /Welcome to OctoFit Tracker/i });
  expect(headingElement).toBeInTheDocument();
});
