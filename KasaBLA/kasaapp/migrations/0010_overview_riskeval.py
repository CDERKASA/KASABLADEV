# Generated by Django 3.1.2 on 2021-04-27 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('kasaapp', '0009_remove_unitoperation_descriptor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('application_path', models.CharField(max_length=100)),
                ('review_decision', models.CharField(max_length=100)),
                ('bla_number', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('applicant_name', models.CharField(max_length=200)),
                ('prop_name', models.CharField(max_length=200)),
                ('non_prop_name', models.CharField(max_length=500)),
                ('obp_name', models.CharField(max_length=500)),
                ('dosage_form', models.CharField(max_length=500)),
                ('strength_potency', models.CharField(max_length=500)),
                ('route_administration', models.CharField(max_length=500)),
                ('primary_assessor', models.CharField(max_length=500)),
                ('secondary_assessor', models.CharField(max_length=500)),
                ('review_iteration', models.CharField(max_length=500)),
                ('review', models.CharField(max_length=500)),
                ('designation', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'kasaapp_overview',
            },
        ),
        migrations.CreateModel(
            name='Riskeval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitop_text', models.CharField(max_length=1000, null=True)),
                ('unitop_ircomments', models.TextField(max_length=1000, null=True)),
                ('harvest_descriptor', models.CharField(max_length=300, null=True)),
                ('harvest_type_unit', models.CharField(max_length=50, null=True)),
                ('chrom_descr_1', models.CharField(max_length=300, null=True)),
                ('chrom_descr_1_unit', models.CharField(max_length=50, null=True)),
                ('chrom_descr_2', models.CharField(max_length=300, null=True)),
                ('chrom_descr_2_unit', models.CharField(max_length=50, null=True)),
                ('chrom_descr_3', models.CharField(max_length=300, null=True)),
                ('chrom_descr_3_unit', models.CharField(max_length=50, null=True)),
                ('chrom_descr_4', models.CharField(max_length=300, null=True)),
                ('chrom_descr_4_unit', models.CharField(max_length=50, null=True)),
                ('chrom_descr_5', models.CharField(max_length=300, null=True)),
                ('chrom_descr_5_unit', models.CharField(max_length=50, null=True)),
                ('chrom_descr_6', models.CharField(max_length=300, null=True)),
                ('chrom_descr_6_unit', models.CharField(max_length=50, null=True)),
                ('chrom_descr_7', models.CharField(max_length=300, null=True)),
                ('chrom_descr_7_unit', models.CharField(max_length=50, null=True)),
                ('chrom_descr_8', models.CharField(max_length=300, null=True)),
                ('chrom_descr_8_unit', models.CharField(max_length=50, null=True)),
                ('chrom_descr_9', models.CharField(max_length=300, null=True)),
                ('chrom_descr_9_unit', models.CharField(max_length=50, null=True)),
                ('new_descriptor', models.CharField(max_length=300, null=True)),
                ('newdescriptor_unit', models.CharField(max_length=50, null=True)),
                ('uf_df_membrane_type', models.CharField(max_length=300, null=True)),
                ('membrane_unit', models.CharField(max_length=50, null=True)),
                ('uf_df_mht', models.CharField(max_length=300, null=True)),
                ('micro_holdtime_unit', models.CharField(max_length=50, null=True)),
                ('uf_df_bht', models.CharField(max_length=300, null=True)),
                ('biochem_holdtime_unit', models.CharField(max_length=50, null=True)),
                ('uf_df_ipt', models.CharField(max_length=300, null=True)),
                ('inprocess_unit', models.CharField(max_length=50, null=True)),
                ('thaw_celltype', models.CharField(max_length=300, null=True)),
                ('celltype_unit', models.CharField(max_length=50, null=True)),
                ('thaw_vessel_type', models.CharField(max_length=300, null=True)),
                ('vessel_unit', models.CharField(max_length=50, null=True)),
                ('thaw_expansion_type', models.CharField(max_length=300, null=True)),
                ('expansion_unit', models.CharField(max_length=50, null=True)),
                ('thaw_ipt', models.CharField(max_length=300, null=True)),
                ('inprocess_thaw_unit', models.CharField(max_length=50, null=True)),
                ('prodbio_media_type', models.CharField(max_length=300, null=True)),
                ('media_type_unit', models.CharField(max_length=50, null=True)),
                ('prodbio_vessel_volume', models.CharField(max_length=300, null=True)),
                ('vessel_volume_unit', models.CharField(max_length=50, null=True)),
                ('prodbio_composition', models.CharField(max_length=300, null=True)),
                ('composition_unit', models.CharField(max_length=50, null=True)),
                ('prodbio_ipt', models.CharField(max_length=300, null=True)),
                ('prodbioinprocess_unit', models.CharField(max_length=50, null=True)),
                ('lowph_acid', models.CharField(max_length=300, null=True)),
                ('acid_unit', models.CharField(max_length=50, null=True)),
                ('lowph_base', models.CharField(max_length=300, null=True)),
                ('base_unit', models.CharField(max_length=50, null=True)),
                ('lowph_mht', models.CharField(max_length=300, null=True)),
                ('micro_holdtime_lowph_unit', models.CharField(max_length=50, null=True)),
                ('lowph_bht', models.CharField(max_length=300, null=True)),
                ('biochem_holdtime_lowph_unit', models.CharField(max_length=50, null=True)),
                ('lowph_ipt', models.CharField(max_length=300, null=True)),
                ('inprocess_lowph_unit', models.CharField(max_length=50, null=True)),
                ('detergent_type', models.CharField(max_length=300, null=True)),
                ('detergent_unit', models.CharField(max_length=50, null=True)),
                ('detergent_mht', models.CharField(max_length=300, null=True)),
                ('micro_holdtime_det_unit', models.CharField(max_length=50, null=True)),
                ('detergent_bht', models.CharField(max_length=300, null=True)),
                ('biochem_holdtime_det_unit', models.CharField(max_length=50, null=True)),
                ('detergent_ipt', models.CharField(max_length=300, null=True)),
                ('inprocess_det_unit', models.CharField(max_length=50, null=True)),
                ('fil_filter', models.CharField(max_length=300, null=True)),
                ('filter_unit', models.CharField(max_length=50, null=True)),
                ('fil_filter_type', models.CharField(max_length=300, null=True)),
                ('fil_filter_unit', models.CharField(max_length=50, null=True)),
                ('fil_ipt', models.CharField(max_length=300, null=True)),
                ('inprocess_viral_unit', models.CharField(max_length=50, null=True)),
                ('seedbio_comp', models.CharField(max_length=300, null=True)),
                ('seed_bio_composition_unit', models.CharField(max_length=50, null=True)),
                ('seedbio_mediatype', models.CharField(max_length=300, null=True)),
                ('seedbio_media_unit', models.CharField(max_length=50, null=True)),
                ('seedbio_ipt', models.CharField(max_length=300, null=True)),
                ('seedbio_inprocess_unit', models.CharField(max_length=50, null=True)),
                ('procname_text', models.CharField(max_length=300, null=True)),
                ('procir_ircomments', models.TextField(max_length=2000, null=True)),
                ('new_parameter', models.CharField(max_length=300, null=True)),
                ('ircomments_newproc', models.TextField(max_length=2000, null=True)),
                ('OBP', models.CharField(max_length=50, null=True)),
                ('obprisk_ircomments', models.TextField(max_length=2000, null=True)),
                ('applicant_risk_ranking', models.CharField(max_length=50, null=True)),
                ('ircomments_apprisk', models.TextField(max_length=2000, null=True)),
                ('new_proc_comment', models.CharField(max_length=300, null=True)),
                ('applicant_risktext', models.CharField(max_length=100, null=True)),
                ('Assign_Risk', models.CharField(max_length=100, null=True)),
                ('CPP_KPP', models.CharField(max_length=100, null=True)),
                ('cpp_ircomments', models.TextField(max_length=2000, null=True)),
                ('applicant_risk2', models.CharField(max_length=100, null=True)),
                ('surr_applicant_risk_ranking', models.CharField(max_length=300, null=True)),
                ('ircomments_surrir', models.TextField(max_length=2000, null=True)),
                ('surprocessparameter', models.CharField(max_length=100, null=True)),
                ('surrproc_ircomments', models.TextField(max_length=2000, null=True)),
                ('app_sur', models.CharField(max_length=100, null=True)),
                ('ircomments_surrapp_risk', models.TextField(max_length=2000, null=True)),
                ('surriskselect', models.CharField(max_length=100, null=True)),
                ('risk_comment', models.CharField(max_length=100, null=True)),
                ('surrisk_text', models.CharField(max_length=100, null=True)),
                ('surr_Assign_Risk', models.CharField(max_length=100, null=True)),
                ('surrCPP_surrKPP', models.CharField(max_length=100, null=True)),
                ('ircomments_surrcpp', models.TextField(max_length=2000, null=True)),
                ('surrisk_text2', models.CharField(max_length=100, null=True)),
                ('cppdropdownselect', models.CharField(max_length=2000, null=True)),
                ('characir_comments', models.TextField(max_length=2000, null=True)),
                ('study_appropriate_select', models.TextField(max_length=2000, null=True)),
                ('appro_charac_ircomments', models.TextField(max_length=2000, null=True)),
                ('characterization_study_pk', models.TextField(max_length=2000, null=True)),
                ('pk_ircomments', models.TextField(max_length=2000, null=True)),
                ('charac_range_low', models.CharField(max_length=50, null=True)),
                ('charac_range_high', models.CharField(max_length=50, null=True)),
                ('charac_range_ircomments', models.TextField(max_length=2000, null=True)),
                ('validation_select', models.TextField(max_length=2000, null=True)),
                ('prelir_ircomments', models.TextField(max_length=2000, null=True)),
                ('valid_range_low', models.CharField(max_length=50, null=True)),
                ('valid_range_high', models.CharField(max_length=50, null=True)),
                ('ircommentsvalrange', models.TextField(max_length=2000, null=True)),
                ('par_ircomments', models.TextField(max_length=2000, null=True)),
                ('par_range_low', models.CharField(max_length=50, null=True)),
                ('par_range_high', models.CharField(max_length=50, null=True)),
                ('response_select', models.TextField(max_length=2000, null=True)),
                ('pp_range_select', models.TextField(max_length=2000, null=True)),
                ('ircommentsprop_par', models.TextField(max_length=2000, null=True)),
                ('bla_number',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kasaapp.overview')),
            ],
            options={
                'db_table': 'kasaapp_Riskeval',
            },
        ),
    ]
