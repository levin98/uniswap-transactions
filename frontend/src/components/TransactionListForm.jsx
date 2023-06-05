import React from "react";
import PropTypes from 'prop-types';
import { Button, DatePicker, Form, Input } from 'antd';
import 'antd/es/date-picker/style/index';
import 'antd/es/input/style/index';

const { RangePicker } = DatePicker;

const TransactionListForm = ({ onSubmit }) => {
    const [form] = Form.useForm();

    return (
        <Form form={form} layout='inline' onFinish={values => onSubmit(values)} data-testid="form">
            <Form.Item label="Transaction Hash" name="hash">
                <Input type="text" placeholder="Txn Hash" data-testid="form-hash" />
            </Form.Item>
            <Form.Item label="Time Range" name="timerange">
                <RangePicker data-testid="form-timerange" />
            </Form.Item>
            <Form.Item>
                <Button className="bg-[#282c34] text-white" htmlType="submit" data-testid="form-submit-button">Submit</Button>
            </Form.Item>
        </Form>
    );
}

TransactionListForm.propTypes = {
    onSubmit: PropTypes.func.isRequired
}

export default TransactionListForm;