import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';
import "./mock"

// eslint-disable-next-line react/display-name
jest.mock('./components/TransactionList', () => () => <div data-testid="transaction-list">Mocked Transaction List</div>);

test('renders App with Transaction List', () => {
  const { container } = render(<App />);
  expect(screen.getByTestId("transaction-list")).toBeInTheDocument();
  expect(container).toMatchSnapshot();
});
