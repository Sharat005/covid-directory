import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { getUserinfo } from '../../actions/userinfo';

export class Userinfo extends Component {
    static propTypes = {
        userinfo: PropTypes.array.isRequired,
        getUserinfo: PropTypes.func.isRequired,
    }

    componentDidMount() {
        this.props.getUserinfo();
    }

    render() {
        return (
            <div>
                <h1>User Info Form</h1>
            </div>
        )
    }
}

const mapStateToProps = (state) => ({
    userinfo: state.userinfo.userinfo,
});

export default connect(mapStateToProps, { getUserinfo })(Userinfo);
