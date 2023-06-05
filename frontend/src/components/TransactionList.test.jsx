import React from 'react';
import { render, screen } from '@testing-library/react';
import TransactionList from './TransactionList';
import "../mock"

// eslint-disable-next-line react/display-name
jest.mock('./TransactionStatistics', () => () => <div data-testid="transaction-statistics">Mocked Transaction Statistics</div>);

// eslint-disable-next-line react/display-name
jest.mock('./TransactionListForm', () => () => <div data-testid="transaction-list-form">Mocked Transaction List Form</div>);

jest.spyOn(window, "fetch").mockImplementation(() => ({}));

test('renders statistics', async () => {
    const { container } = render(<TransactionList />);

    const list = await screen.findByTestId("transaction-list-form");
    const statistics = await screen.findByTestId("transaction-statistics");
    expect(list).toBeInTheDocument();
    expect(statistics).toBeInTheDocument();
    expect(container).toMatchSnapshot();
});
