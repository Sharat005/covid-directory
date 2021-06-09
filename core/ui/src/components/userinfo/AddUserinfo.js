import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addUserinfo } from '../../actions/userinfo';
import { DEFUALT_USERFORM_STATE, PHONE1_TYPE_OPTIONS, YES_NO_OPTIONS } from '../../utils/form-helper';
import { PHONE2_TYPE_OPTIONS, RECRUITMENT_SOURCE_OPTIONS, STATES, GENDER, RACE, ETHNICITY } from '../../utils/form-helper';
import TextInputComponent from '../form-components/text-input';
import { DatePickerComponent } from '../form-components/date-picker';
import DropdownComponent from '../form-components/dropdown';

export class AddUserinfo extends Component {
    state = DEFUALT_USERFORM_STATE;

    static propTypes = {
        addUserinfo: PropTypes.func.isRequired,
    }

    onChange = e => this.setState({ [e.target.name]: e.target.value });
    onDateChange = (key, date) => this.setState({ [key]: date.toISOString().split('T')[0]});
    onSubmit = e => {
        e.preventDefault();

        this.state.dob = this.state.dob.toISOString().split('T')[0];

        const { name_first, name_middle, name_last, dob, phone1, phone1_type, phone1_text_yn, contact_basetime_survey, phone2, phone2_type, phone2_text_yn, address1, address2, city, state, zipcode, voicemail_yn_survey, copd_yn_survey, copd_exacerbation_yn_survey, smoking_yn_survey, smoking_now_yn_survey, smoking_start_survey, smoking_stop_survey, smoking_amount_survey, rx_bp_yn_survey, rx_bp_survey, recruitment_source_survey, recruitment_source_other_survey, current_age, gender, race, ethnicity, email_yn, email } = this.state;

        
        const userInfo = { name_first, name_middle, name_last, dob, phone1, phone1_type, phone1_text_yn, contact_basetime_survey, phone2, phone2_type, phone2_text_yn, address1, address2, city, state, zipcode, voicemail_yn_survey, copd_yn_survey, copd_exacerbation_yn_survey, smoking_yn_survey, smoking_now_yn_survey, smoking_start_survey, smoking_stop_survey, smoking_amount_survey, rx_bp_yn_survey, rx_bp_survey, recruitment_source_survey, recruitment_source_other_survey, current_age, gender, race, ethnicity, email_yn, email };

        this.props.addUserinfo(userInfo);
        console.log("submit");
    }

    render() {
        const { name_first, name_middle, name_last, dob, phone1, phone1_type, phone1_text_yn, contact_basetime_survey, phone2, phone2_type, phone2_text_yn, address1, address2, city, state, zipcode, voicemail_yn_survey, copd_yn_survey, copd_exacerbation_yn_survey, smoking_yn_survey, smoking_now_yn_survey, smoking_start_survey, smoking_stop_survey, smoking_amount_survey, rx_bp_yn_survey, rx_bp_survey, recruitment_source_survey, recruitment_source_other_survey, current_age, gender, race, ethnicity, email_yn, email } = this.state;

        return (
            <div className="card card-body mt-4 mb-4">
                <h2>Add Patient Information</h2>
                <form onSubmit={this.onSubmit}>
                    {/* First Name */}
                    <TextInputComponent label="First Name" name="name_first" value={name_first} action={this.onChange} /> <br />
                    <TextInputComponent label="Middle Name" name="name_middle" value={name_middle} action={this.onChange} /> <br />
                    <TextInputComponent label="Last Name" name="name_last" value={name_last} action={this.onChange} /> <br />

                    {/* <DatePickerComponent label="Date of Birth" name="dob" value={Date(dob)} onChange={this.onDateChange} /> <br /> */}

                    {/* Phone 1 */}
                    <TextInputComponent name="phone1" value={phone1} action={this.onChange} /> <br />
                    <DropdownComponent name="phone1_type" value={phone1_type} onChange={this.onChange} options={PHONE1_TYPE_OPTIONS}/> <br />
                    <DropdownComponent name="phone1_text_yn" value={phone1_text_yn} onChange={this.onChange} options={YES_NO_OPTIONS}/> <br />

                    {/* Basetime contact AM/PM */}
                    <DropdownComponent name="contact_basetime_survey" value={contact_basetime_survey} onChange={this.onChange} options={YES_NO_OPTIONS}/> <br />

                    {/* Phone 2 */}
                    <TextInputComponent name="phone2" value={phone2} action={this.onChange} /> <br />
                    <DropdownComponent name="phone2_type" value={phone2_type} onChange={this.onChange} options={PHONE2_TYPE_OPTIONS}/> <br />
                    <DropdownComponent name="phone2_text_yn" value={phone2_text_yn} onChange={this.onChange} options={YES_NO_OPTIONS}/> <br />

                    {/* Address, City, State, Zip */}
                    <TextInputComponent name="address1" value={address1} action={this.onChange} /> <br />
                    <TextInputComponent name="address2" value={address2} action={this.onChange} /> <br />
                    <TextInputComponent name="city" value={city} action={this.onChange} /> <br />
                    <DropdownComponent name="state" value={state} onChange={this.onChange} options={STATES}/> <br />
                    <TextInputComponent name="zipcode" value={zipcode} action={this.onChange} /> <br />

                    {/* voicemail y/n */}
                    <DropdownComponent name="voicemail_yn_survey" value={voicemail_yn_survey} onChange={this.onChange} options={YES_NO_OPTIONS}/> <br />
                    {/* copd y/n */}
                    <DropdownComponent name="copd_yn_survey" value={copd_yn_survey} onChange={this.onChange} options={YES_NO_OPTIONS}/> <br />
                    {/* ever smoked y/n */}
                    <DropdownComponent name="smoking_yn_survey" value={smoking_yn_survey} onChange={this.onChange} options={YES_NO_OPTIONS}/> <br />
                    {/* bp medicines */}
                    <DropdownComponent name="rx_bp_yn_survey" value={rx_bp_yn_survey} onChange={this.onChange} options={YES_NO_OPTIONS}/> <br />
                    {/* Recruitment Source */}
                    <DropdownComponent name="recruitment_source_survey" value={recruitment_source_survey} onChange={this.onChange} options={RECRUITMENT_SOURCE_OPTIONS}/> <br />

                    {/* Gender, Race, Ethnicity */}
                    <DropdownComponent name="gender" value={gender} onChange={this.onChange} options={GENDER}/> <br />
                    <DropdownComponent name="race" value={race} onChange={this.onChange} options={RACE}/> <br />
                    <DropdownComponent name="ethnicity" value={ethnicity} onChange={this.onChange} options={ETHNICITY}/> <br />

                    {/* Email */}
                    <DropdownComponent name="email_yn" value={email_yn} onChange={this.onChange} options={YES_NO_OPTIONS}/> <br />

                    <div className="form-group">
                        <button type="submit" className="btn btn-primary"> Submit </button>
                    </div>
                </form>
            </div>
        )
    }
}

export default connect(null, { addUserinfo })(AddUserinfo);
