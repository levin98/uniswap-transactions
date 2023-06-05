import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import { Card, Col, Row, Statistic, Alert } from 'antd';

const TransactionStatistics = ({ transactionList }) => {
    const [error, setError] = useState('');
    const [price, setPrice] = useState(0);

    const getTotalFeeinETH = () => {
        return transactionList.reduce((acc, curr) => {
            return acc + (parseFloat(curr.gas_used) * parseFloat(curr.gas_price)) * Math.pow(10, -18);
        }, 0)
    }

    const getTickerPrice = async () => {
        setError('');
        try {
            const response = await fetch("https://data-api.binance.vision/api/v3/ticker/price?symbol=ETHUSDT");
            const data = await response.json();
            setPrice(data.price);
        } catch (e) {
            setError(e.message);
        }
    }

    useEffect(() => {
        let id = setTimeout(getTickerPrice, 1000);
        return () => clearTimeout(id);
    });

    return (
        <>
            {error && <Alert message={error} type="error" showIcon style={{ marginBottom: '10px' }} />}
            <Row gutter={16}>
                <Col span={8}>
                    <Card><Statistic title="Total Transaction Fee (USDT)" value={getTotalFeeinETH() * price} /></Card>
                </Col>
                <Col span={8}>
                    <Card><Statistic title="Total Transaction Fee (ETH)" value={getTotalFeeinETH()} /></Card>
                </Col>
                <Col span={8}>
                    <Card><Statistic title="ETH/USDT" value={price} /></Card>
                </Col>
            </Row>
        </>
    )
};

TransactionStatistics.propTypes = {
    transactionList: PropTypes.array
}

TransactionStatistics.defaultProps = {
    transactionList: []
}

export default TransactionStatistics;