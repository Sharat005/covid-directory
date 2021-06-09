import React, { Component, useState } from 'react'
import DatePicker from "react-datepicker";
import PropTypes from 'prop-types';
require("react-datepicker/dist/react-datepicker.css");

export class DatePickerComponent extends Component {

    static propTypes = {
        name: PropTypes.string.isRequired,
        label: PropTypes.string.isRequired,
        value: PropTypes.object.isRequired,
        onChange: PropTypes.any.isRequired
    }

    render() {
        return (
            <FormControl style={{minWidth: 200}}>
                <InputLabel htmlFor={this.props.name}>{FORM_LABEL[this.props.name]}</InputLabel>

                {/* <label htmlFor={this.props.name}>{this.props.label}: </label> */}
                <DatePicker
                    name={this.props.name}
                    dateFormat="yyyy/MM/dd"
                    value={this.props.value}
                    onChange={this.props.onChange.bind(this, this.props.name)}
                        />
            </FormControl>
        )
    }
}

export default DatePickerComponent
