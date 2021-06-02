# Generated by Django 3.2.3 on 2021-06-02 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screen_age_yn', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], verbose_name='Are you between the ages 40-80?')),
                ('screen_age', models.IntegerField(blank=True, null=True, verbose_name='Specify age:')),
                ('screen_gender', models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female'), (3, 'Refused')], null=True, verbose_name='Please confirm your gender')),
                ('screen_smoking_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Are you a current or former smoker?')),
                ('screen_smoking_amount', models.IntegerField(blank=True, null=True, verbose_name='On average, how many packs do or did you smoke per day?')),
                ('screen_smoking_years', models.IntegerField(blank=True, null=True, verbose_name='How many years have you (or had you) smoked?')),
                ('screen_packyears', models.IntegerField(blank=True, null=True, verbose_name='Packyear Calculation Result')),
                ('screen_20packyears_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='B1b. Based on your calculation, does the subject have 10 pack-year smoking history?')),
                ('screen_pregnancy_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='(FEMALES ONLY) Are you pregnant, breast-feeding, or planning to become pregnant in the next 3 months?')),
                ('screen_rx_respiratoryinfection_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='C2. Have you received a course of antibiotics or systemic steroids for respiratory infection within the past 4 weeks?')),
                ('screen_hx_asthma_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Do you have a history of asthma?')),
                ('screen_hx_asthma_age', models.IntegerField(blank=True, null=True, verbose_name='Please provide age when diagnosed.')),
                ('screen_hx_lungdisease_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Do you have a history of lung disease?')),
                ('screen_hx_lungdisease', models.CharField(blank=True, max_length=300, verbose_name='Please specify')),
                ('screen_diabetes_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Do you have Diabetes Type I?')),
                ('screen_lungcancer_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Do you have lung cancer or a history of lung cancer?')),
                ('screen_dx_additional_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Do you have narrow-angle glaucoma, bladder-neck obstruction or severe renal impairment or urinary retention?')),
                ('screen_investigationaldrug_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Are you currently or have you in the past 30 days participated in any other clinical trials involving an investigational drug?')),
                ('screen_hx_atrialfibrillation_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Do you have a history of atrial fibrillation?')),
                ('screen_therapy_atrialfibrillation_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Have you been on therapy for your atrial fibrillation for 6 months or more?')),
                ('screen_treatment_atrialfibrillation_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Has your atrial fibrillation been well controlled with treatment for 6 months or more?')),
                ('screen_bph_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Do you have Benign Prostatic Hyperplasia (BPH)?')),
                ('screen_treatment_bph_yn', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes')], null=True, verbose_name='Do you have Benign Prostatic Hyperplasia (BPH)?')),
                ('screen_comments', models.CharField(blank=True, max_length=300, verbose_name='Any other information would you like to provide.')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.patientinfo', verbose_name='Patient ID')),
            ],
        ),
    ]
