export const DEFUALT_USERFORM_STATE = {
    name_first: "",
    name_middle: "",
    name_last: "",
    dob: new Date(),
    phone1: "",
    phone1_type: "",
    phone1_text_yn: "",
    contact_basetime_survey: "",
    phone2: "",
    phone2_type: "",
    phone2_text_yn: "",
    address1: "",
    address2: "",
    city: "",
    state: "",
    zipcode: "",
    voicemail_yn_survey: "",
    copd_yn_survey: "",
    copd_exacerbation_yn_survey: null,
    smoking_yn_survey: "",
    smoking_now_yn_survey: null,
    smoking_start_survey: null,
    smoking_stop_survey: null,
    smoking_amount_survey: null,
    rx_bp_yn_survey: "",
    rx_bp_survey: "",
    recruitment_source_survey: "",
    recruitment_source_other_survey: "",
    current_age: null,
    gender: "",
    race: "",
    ethnicity: "",
    email_yn: "",
    email: ""
};

export const DEFAULT_SCREEN_STATE =  {
    "patient": -1,
    "screen_age_yn": "",
    "screen_age": "",
    "screen_gender": "",
    "screen_smoking_yn": "",
    "screen_smoking_amount": "",
    "screen_smoking_years": "",
    "screen_packyears": "",
    "screen_20packyears_yn": "",
    "screen_pregnancy_yn": "",
    "screen_rx_respiratoryinfection_yn": "",
    "screen_hx_asthma_yn": "",
    "screen_hx_asthma_age": "",
    "screen_hx_lungdisease_yn": "",
    "screen_hx_lungdisease": "",
    "screen_diabetes_yn": "",
    "screen_lungcancer_yn": "",
    "screen_dx_additional_yn": "",
    "screen_investigationaldrug_yn": "",
    "screen_hx_atrialfibrillation_yn": "",
    "screen_therapy_atrialfibrillation_yn": "",
    "screen_treatment_atrialfibrillation_yn": "",
    "screen_bph_yn": "",
    "screen_treatment_bph_yn": "",
    "screen_comments": "",
}



export const PHONE1_TYPE_OPTIONS = [["1","Landline"], ["2","Cell"]];
export const PHONE2_TYPE_OPTIONS = [["1","Home"], ["2","Cell"]];
export const YES_NO_OPTIONS = [["0", "No"], ["1", "Yes"]];
export const RECRUITMENT_SOURCE_OPTIONS = [["1", "Facebook"], ["2", "Instagram"], ["3", "Email"], ["4", "Flyers"], ["5", "Craigslist"], ["6", "Referral"], ["99", "Other"],];
export const RACE = [["1", "American Indian/Alaskan Native"], ["2", "Asian"], ["3", "Black/African American"], ["4", "Native Hawaiian/Pacific Islander"], ["5", "Whtie"], ["6", "Other"], ["7", "Unknown"], ];
export const GENDER = [["1", "Male"], ["2", "Female"], ["3","Refused"]];
export const ETHNICITY = [["1", "Hispanic/Latino"], ["2", "Not Hispanic/Latino"], ["3", "Unknown"]];
export const STATES = [["13", "Illinois"], ["1", "Alabama"], ["2", "Alaska"], ["3", "Arizona"], ["4", "Arkansas"], ["5", "California"], ["6", "Colorado"], ["7", "Connecticut"], ["8", "Delaware"], ["9", "Florida"], ["10", "Georgia"], ["11", "Hawaii"], ["12", "Idaho"], ["14", "Indiana"], ["15", "Iowa"], ["16", "Kansas"], ["17", "Kentucky"], ["18", "Louisiana"], ["19", "Maine"], ["20", "Maryland"], ["21", "Massachusetts"], ["22", "Michigan"], ["23", "Minnesota"], ["24", "Mississippi"], ["25", "Missouri"], ["26", "Montana"], ["27", "Nebraska"], ["28", "Nevada"], ["29", "New Hampshire"], ["30", "New Jersey"], ["31", "New Mexico"], ["32", "New York"], ["33", "North Carolina"], ["34", "North Dakota"], ["35", "Ohio"], ["36", "Oklahoma"], ["37", "Oregon"], ["38", "Pennsylvania"], ["39", "Rhode Island"], ["40", "South Carolina"], ["41", "South Dakota"], ["42", "Tennessee"], ["43", "Texas"], ["44", "Utah"], ["45", "Vermont"], ["46", "Virginia"], ["47", "Washington"], ["48", "West Virginia"], ["49", "Wisconsin"], ["50", "Wyoming"]];

export const FORM_LABEL = {
    "name_first": "First Name",
    "name_last": "Last Name",
    "name_middle": "Middle Name",
    "phone1": "Primary Phone",
    "phone1_type": "Phone Type",
    "phone1_text_yn": "Are you willing to receive text messages at this number?",
    "contact_basetime_survey": "When is the best time to contact you?",
    "phone2": "Secondary Phone",
    "phone2_type": "Phone Type",
    "phone2_type": "Phone Type",
    "phone2_text_yn": "Are you willing to receive text messages at this number?",
    "address1": "Address1 (Building no. & Street name)",
    "address2": "Address2 (if applicable, Unit/Apt name)",
    "city": "City",
    "state": "State",
    "zipcode": "Zipcode",
    "voicemail_yn_survey":"May the UIC Breathe Chicago Center leave you a voicemail the above number?", 
    "copd_yn_survey":"Has a doctor told you that you have Chronic Obstructive Pulmonary Disease (COPD)?",
    "smoking_yn_survey":"Have you ever smoked cigarettes?",
    "rx_bp_yn_survey":"Are you using any blood pressure medicines?",
    "recruitment_source_survey":"Where did you hear about us?",
    "gender":"Gender",
    "race": "Race",
    "ethnicity": "Ethnicity",
    "email_yn": "Do you have an email address?"
}