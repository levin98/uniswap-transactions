import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import TransactionListForm from './TransactionListForm';
import "../mock"

test('renders the form', () => {
    const { container } = render(<TransactionListForm onSubmit={jest.fn()} />);

    expect(screen.getByTestId("form")).toBeInTheDocument();
    expect(screen.getByTestId("form-hash")).toBeInTheDocument();
    expect(screen.getByTestId("form-timerange")).toBeInTheDocument();
    expect(screen.getByTestId("form-submit-button")).toBeInTheDocument();
    expect(container).toMatchSnapshot();
});

test('calls onSubmit with the form values', async () => {
    const onSubmit = jest.fn();
    render(<TransactionListForm onSubmit={onSubmit} />);

    fireEvent.submit(screen.getByText("Submit"));
    await waitFor(() => expect(onSubmit).toHaveBeenCalledTimes(1));
});