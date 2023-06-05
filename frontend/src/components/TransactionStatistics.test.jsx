import React from 'react';
import { render, screen } from '@testing-library/react';
import TransactionStatistics from './TransactionStatistics';
import "../mock"

jest.spyOn(window, "fetch").mockImplementation(() => ({ "price": 1000 }));

const mockData = [
    {
        "gasPrice": "19156218168",
        "gasUsed": "422092",
    },
    {
        "gasPrice": "19992909881",
        "gasUsed": "210998",
    }
]

test('renders statistics', () => {
    const { container } = render(<TransactionStatistics transactionList={mockData} />);

    expect(screen.getByText("Total Transaction Fee (USDT)")).toBeInTheDocument();
    expect(screen.getByText("Total Transaction Fee (ETH)")).toBeInTheDocument();
    expect(screen.getByText("ETH/USDT")).toBeInTheDocument();
    expect(container).toMatchSnapshot();
});
