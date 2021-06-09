import React, { Component } from 'react'
import PropTypes from 'prop-types'
import { FormControl, InputLabel } from '@material-ui/core';
import { FORM_LABEL } from '../../utils/form-helper'

export class TextInputComponent extends Component {
    static defaultProps = {

    }

    static propTypes = {
        name: PropTypes.string.isRequired,
        value: PropTypes.string.isRequired,
        action: PropTypes.any.isRequired,
    }

    render() {
        return (
            <div className="form-group">
                <label> {FORM_LABEL[this.props.name]} </label>
                <input
                    className="form-control"
                    type="text"
                    name={this.props.name}
                    value={this.props.value}
                    onChange={this.props.action}
                />
            </div>
        )
    }
}

export default TextInputComponent
