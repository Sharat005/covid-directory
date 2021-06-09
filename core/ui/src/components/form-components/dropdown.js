import React, { Component } from 'react'
import MenuItem from '@material-ui/core/MenuItem';
import { FormControl, InputLabel } from '@material-ui/core';
import Select from '@material-ui/core/Select';
import PropTypes from 'prop-types';
import { FORM_LABEL } from '../../utils/form-helper';

export class DropdownComponent extends Component {

    static propTypes = {
        name: PropTypes.string.isRequired,
        options: PropTypes.array.isRequired,
        value: PropTypes.string.isRequired,
        onChange: PropTypes.any.isRequired
    }

    render() {
        const menuItems = [];
        for (const [index, option] of this.props.options) {
            menuItems.push(
                <MenuItem key={option} value={index}>
                    {option}
                </MenuItem>);
        }

        return (
            <FormControl style={{minWidth: 700}}>
                <InputLabel htmlFor={this.props.name}>{FORM_LABEL[this.props.name]}</InputLabel>
                <Select
                    name={this.props.name}
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={this.props.value}
                    onChange={this.props.onChange}>
                    {menuItems}
                </Select>
            </FormControl>
        )
    }
}

export default DropdownComponent
