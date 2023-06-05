import React, { useState, useEffect } from 'react';
import { Card, Table, Alert, Pagination, Divider } from 'antd';
import TransactionListForm from './TransactionListForm';
import TransactionStatistics from './TransactionStatistics';

const columns = [
    {
        title: 'Transaction Hash',
        dataIndex: 'txn_hash',
        key: 'txn_hash',
    },
    {
        title: 'Block Number',
        dataIndex: 'block_number',
        key: 'block_number',
    },
    {
        title: 'Timestamp',
        dataIndex: 'txn_timestamp',
        key: 'txn_timestamp',
    },
    {
        title: 'Transaction Fee',
        dataIndex: 'gas_used',
        key: 'gas_used',
        render: (gas_used, row) => {
            return `${(parseFloat(gas_used) * parseFloat(row.gas_price)) * Math.pow(10, -18)} ETH`
        }
    }
]

const TransactionList = () => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const [hash, setHash] = useState('');
    const [from, setFrom] = useState('');
    const [to, setTo] = useState('');

    const [page, setPage] = useState(1);
    const [pageSize, setPageSize] = useState(50);
    const [count, setCount] = useState(0);

    const getTransactions = async (h = hash, f = from, t = to) => {
        setLoading(true);
        setError('');
        try {
            if (h !== "") {
                const response = await fetch(`http://localhost:5000/transaction?hash=${h}`);
                const data = await response.json();
                if (response.status === 404) {
                    setError("Transaction not found");
                    setData([]);
                    setCount(0);
                    return;
                }
                setData([data]);
                setCount(1);
            } else {
                const response = await fetch(`http://localhost:5000/transactions?page=${page}&pageSize=${pageSize}&from=${f}&to=${t}`);
                const data = await response.json();
                setData(data.results);
                setCount(data.pagination.count);
            }
        } catch (e) {
            setError(e.message);
        } finally {
            setLoading(false);
        }
    }

    useEffect(() => {
        getTransactions();
    }, [page, pageSize]);

    const onChangePagination = (page, pageSize) => {
        setPage(page);
        if (pageSize) {
            setPageSize(pageSize);
        }
    }

    const onSubmit = async (values) => {
        setHash(values.hash);
        if (values.timerange) {
            setFrom(values.timerange[0].unix());
            setTo(values.timerange[1].unix());
        }
        await getTransactions(values.hash, values.timerange ? values.timerange[0].unix() : '', values.timerange ? values.timerange[1].unix() : '');
    }

    return (
        <Card className="h-[90vh] w-[90vw]">
            <TransactionStatistics transactionList={data} />
            <Divider />
            <TransactionListForm onSubmit={onSubmit} />
            <br />
            {error && <Alert message={error} type="error" showIcon style={{ marginBottom: '10px' }} />}
            <div className='h-[50vh] overflow-auto'>
                <Table rowKey="txn_hash" columns={columns} loading={loading} dataSource={data} pagination={false} />
            </div>
            <br />
            <div className='text-right'>
                <Pagination current={page} pageSize={pageSize} total={count} onChange={onChangePagination} pageSizeOptions={[10, 20, 50, 100]} showSizeChanger />
            </div>
        </Card>
    );
}

export default TransactionList;