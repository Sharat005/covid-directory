import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addUserinfo } from '../../actions/userinfo';
import { DEFAULT_SCREEN_STATE, YES_NO_OPTIONS } from '../../utils/form-helper';
import { GENDER, RACE, ETHNICITY } from '../../utils/form-helper';
import TextInputComponent from '../form-components/text-input';
import DropdownComponent from '../form-components/dropdown';

export class Screen extends Component {
    state = DEFAULT_SCREEN_STATE;

    static propTypes = {
        addScreeninfo: PropTypes.func.isRequired;
    }

    onChange = e => this.setState({ [e.target.name]: e.target.value });  

    onSubmit = e => {
        e.preventDefault();
        const { patient, screen_age_yn, screen_age, screen_gender, screen_smoking_yn, screen_smoking_amount, screen_smoking_years, screen_packyears, screen_20packyears_yn, screen_pregnancy_yn, screen_rx_respiratoryinfection_yn, screen_hx_asthma_yn, screen_hx_asthma_age, screen_hx_lungdisease_yn, screen_hx_lungdisease, screen_diabetes_yn, screen_lungcancer_yn, screen_dx_additional_yn, screen_investigationaldrug_yn, screen_hx_atrialfibrillation_yn, screen_therapy_atrialfibrillation_yn, screen_treatment_atrialfibrillation_yn, screen_bph_yn, screen_treatment_bph_yn } = this.state;    

        const screenInfo = { patient, screen_age_yn, screen_age, screen_gender, screen_smoking_yn, screen_smoking_amount, screen_smoking_years, screen_packyears, screen_20packyears_yn, screen_pregnancy_yn, screen_rx_respiratoryinfection_yn, screen_hx_asthma_yn, screen_hx_asthma_age, screen_hx_lungdisease_yn, screen_hx_lungdisease, screen_diabetes_yn, screen_lungcancer_yn, screen_dx_additional_yn, screen_investigationaldrug_yn, screen_hx_atrialfibrillation_yn, screen_therapy_atrialfibrillation_yn, screen_treatment_atrialfibrillation_yn, screen_bph_yn, screen_treatment_bph_yn }

        this.props.addScreeninfo(screenInfo);
        console.log("submit");
    }
    render() {

        const { patient, screen_age_yn, screen_age, screen_gender, screen_smoking_yn, screen_smoking_amount, screen_smoking_years, screen_packyears, screen_20packyears_yn, screen_pregnancy_yn, screen_rx_respiratoryinfection_yn, screen_hx_asthma_yn, screen_hx_asthma_age, screen_hx_lungdisease_yn, screen_hx_lungdisease, screen_diabetes_yn, screen_lungcancer_yn, screen_dx_additional_yn, screen_investigationaldrug_yn, screen_hx_atrialfibrillation_yn, screen_therapy_atrialfibrillation_yn, screen_treatment_atrialfibrillation_yn, screen_bph_yn, screen_treatment_bph_yn } = this.state;    

        return (
            <div className="card card-body mt-4 mb-4">
                <h1>Screen Form</h1>
                <form onSubmit={this.onSubmit}>
                    <TextInputComponent label="Patient ID" name="patient" value={patient} action={this.onChange} />
                    <TextInputComponent label="First Name" name="screen_age_yn" value={screen_age_yn} action={this.onChange} /> <br />

                    <div className="form-group">
                        <button type="submit" className="btn btn-primary"> Submit </button>
                    </div>
                </form>
            </div>
        )
    }
}

export default connect(null, { addScreeninfo })(Screen)
