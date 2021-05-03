from django.db import models


class unitoperation(models.Model):
    unitoperation_name = models.CharField(max_length=300)

    def __str__(self):
        return self.unitoperation_name

    class Meta:
        db_table = 'kasaapp_unitoperation'


class processparameter(models.Model):
    unitoperation = models.ForeignKey(unitoperation, on_delete=models.CASCADE)
    processparameter_name = models.CharField(max_length=300)
    risk_ranking = models.CharField(max_length=200)

    def __str__(self):
        return self.processparameter_name

    class Meta:
        db_table = 'kasaapp_processparameter'


class Overview(models.Model):
    application_path = models.CharField(max_length=100)
    review_decision = models.CharField(max_length=100)
    bla_number = models.CharField(primary_key=True, max_length=100)
    applicant_name = models.CharField(max_length=200)
    prop_name = models.CharField(max_length=200)
    non_prop_name = models.CharField(max_length=500)
    obp_name = models.CharField(max_length=500)
    dosage_form = models.CharField(max_length=500)
    strength_potency = models.CharField(max_length=500)
    route_administration = models.CharField(max_length=500)
    primary_assessor = models.CharField(max_length=500)
    secondary_assessor = models.CharField(max_length=500)
    review_iteration = models.CharField(max_length=500)
    review = models.CharField(max_length=500)
    designation = models.CharField(max_length=500)

    def __str__(self):
        return self.applicant_name

    class Meta:
        db_table = 'kasaapp_overview'


class Riskeval(models.Model):
    bla_number = models.ForeignKey(Overview, null=True, on_delete=models.CASCADE)
    unitop_text = models.CharField(null=True, max_length=1000)
    unitop_ircomments = models.TextField(null=True, max_length=1000)
    harvest_descriptor = models.CharField(null=True, max_length=300)
    harvest_type_unit = models.CharField(null=True, max_length=50)
    chrom_descr_1 = models.CharField(null=True, max_length=300)
    chrom_descr_1_unit = models.CharField(null=True, max_length=50)
    chrom_descr_2 = models.CharField(null=True, max_length=300)
    chrom_descr_2_unit = models.CharField(null=True, max_length=50)
    chrom_descr_3 = models.CharField(null=True, max_length=300)
    chrom_descr_3_unit = models.CharField(null=True, max_length=50)
    chrom_descr_4 = models.CharField(null=True, max_length=300)
    chrom_descr_4_unit = models.CharField(null=True, max_length=50)
    chrom_descr_5 = models.CharField(null=True, max_length=300)
    chrom_descr_5_unit = models.CharField(null=True, max_length=50)
    chrom_descr_6 = models.CharField(null=True, max_length=300)
    chrom_descr_6_unit = models.CharField(null=True, max_length=50)
    chrom_descr_7 = models.CharField(null=True, max_length=300)
    chrom_descr_7_unit = models.CharField(null=True, max_length=50)
    chrom_descr_8 = models.CharField(null=True, max_length=300)
    chrom_descr_8_unit = models.CharField(null=True, max_length=50)
    chrom_descr_9 = models.CharField(null=True, max_length=300)
    chrom_descr_9_unit = models.CharField(null=True, max_length=50)
    new_descriptor = models.CharField(null=True, max_length=300)
    newdescriptor_unit = models.CharField(null=True, max_length=50)
    uf_df_membrane_type = models.CharField(null=True, max_length=300)
    membrane_unit = models.CharField(null=True, max_length=50)
    uf_df_mht = models.CharField(null=True, max_length=300)
    micro_holdtime_unit = models.CharField(null=True, max_length=50)
    uf_df_bht = models.CharField(null=True, max_length=300)
    biochem_holdtime_unit = models.CharField(null=True, max_length=50)
    uf_df_ipt = models.CharField(null=True, max_length=300)
    inprocess_unit = models.CharField(null=True, max_length=50)
    thaw_celltype = models.CharField(null=True, max_length=300)
    celltype_unit = models.CharField(null=True, max_length=50)
    thaw_vessel_type = models.CharField(null=True, max_length=300)
    vessel_unit = models.CharField(null=True, max_length=50)
    thaw_expansion_type = models.CharField(null=True, max_length=300)
    expansion_unit = models.CharField(null=True, max_length=50)
    thaw_ipt = models.CharField(null=True, max_length=300)
    inprocess_thaw_unit = models.CharField(null=True, max_length=50)
    prodbio_media_type = models.CharField(null=True, max_length=300)
    media_type_unit = models.CharField(null=True, max_length=50)
    prodbio_vessel_volume = models.CharField(null=True, max_length=300)
    vessel_volume_unit = models.CharField(null=True, max_length=50)
    prodbio_composition = models.CharField(null=True, max_length=300)
    composition_unit = models.CharField(null=True, max_length=50)
    prodbio_ipt = models.CharField(null=True, max_length=300)
    prodbioinprocess_unit = models.CharField(null=True, max_length=50)
    lowph_acid = models.CharField(null=True, max_length=300)
    acid_unit = models.CharField(null=True, max_length=50)
    lowph_base = models.CharField(null=True, max_length=300)
    base_unit = models.CharField(null=True, max_length=50)
    lowph_mht = models.CharField(null=True, max_length=300)
    micro_holdtime_lowph_unit = models.CharField(null=True, max_length=50)
    lowph_bht = models.CharField(null=True, max_length=300)
    biochem_holdtime_lowph_unit = models.CharField(null=True, max_length=50)
    lowph_ipt = models.CharField(null=True, max_length=300)
    inprocess_lowph_unit = models.CharField(null=True, max_length=50)
    detergent_type = models.CharField(null=True, max_length=300)
    detergent_unit = models.CharField(null=True, max_length=50)
    detergent_mht = models.CharField(null=True, max_length=300)
    micro_holdtime_det_unit = models.CharField(null=True, max_length=50)
    detergent_bht = models.CharField(null=True, max_length=300)
    biochem_holdtime_det_unit = models.CharField(null=True, max_length=50)
    detergent_ipt = models.CharField(null=True, max_length=300)
    inprocess_det_unit = models.CharField(null=True, max_length=50)
    fil_filter = models.CharField(null=True, max_length=300)
    filter_unit = models.CharField(null=True, max_length=50)
    fil_filter_type = models.CharField(null=True, max_length=300)
    fil_filter_unit = models.CharField(null=True, max_length=50)
    fil_ipt = models.CharField(null=True, max_length=300)
    inprocess_viral_unit = models.CharField(null=True, max_length=50)
    seedbio_comp = models.CharField(null=True, max_length=300)
    seed_bio_composition_unit = models.CharField(null=True, max_length=50)
    seedbio_mediatype = models.CharField(null=True, max_length=300)
    seedbio_media_unit = models.CharField(null=True, max_length=50)
    seedbio_ipt = models.CharField(null=True, max_length=300)
    seedbio_inprocess_unit = models.CharField(null=True, max_length=50)
    procname_text = models.CharField(null=True, max_length=300)
    procir_ircomments = models.TextField(null=True, max_length=2000)
    new_parameter = models.CharField(null=True, max_length=300)
    ircomments_newproc = models.TextField(null=True, max_length=2000)
    OBP = models.CharField(null=True, max_length=50)
    obprisk_ircomments = models.TextField(null=True, max_length=2000)
    applicant_risk_ranking = models.CharField(null=True, max_length=50)
    ircomments_apprisk = models.TextField(null=True, max_length=2000)
    new_proc_comment = models.CharField(null=True, max_length=300)
    applicant_risktext = models.CharField(null=True, max_length=100)
    Assign_Risk = models.CharField(null=True, max_length=100)
    CPP_KPP = models.CharField(null=True, max_length=100)
    cpp_ircomments = models.TextField(null=True, max_length=2000)
    applicant_risk2 = models.CharField(null=True, max_length=100)
    surr_applicant_risk_ranking = models.CharField(null=True, max_length=300)
    ircomments_surrir = models.TextField(null=True, max_length=2000)
    surprocessparameter = models.CharField(null=True, max_length=100)
    surrproc_ircomments = models.TextField(null=True, max_length=2000)
    app_sur = models.CharField(null=True, max_length=100)
    ircomments_surrapp_risk = models.TextField(null=True, max_length=2000)
    surriskselect = models.CharField(null=True, max_length=100)
    risk_comment = models.CharField(null=True, max_length=100)
    surrisk_text = models.CharField(null=True, max_length=100)
    surr_Assign_Risk = models.CharField(null=True, max_length=100)
    surrCPP_surrKPP = models.CharField(null=True, max_length=100)
    ircomments_surrcpp = models.TextField(null=True, max_length=2000)
    surrisk_text2 = models.CharField(null=True, max_length=100)
    cppdropdownselect = models.CharField(null=True, max_length=2000)
    characir_comments = models.TextField(null=True, max_length=2000)
    study_appropriate_select = models.TextField(null=True, max_length=2000)
    appro_charac_ircomments = models.TextField(null=True, max_length=2000)
    characterization_study_pk = models.TextField(null=True, max_length=2000)
    pk_ircomments = models.TextField(null=True, max_length=2000)
    charac_range_low = models.CharField(null=True, max_length=50)
    charac_range_high = models.CharField(null=True, max_length=50)
    charac_range_ircomments = models.TextField(null=True, max_length=2000)
    validation_select = models.TextField(null=True, max_length=2000)
    prelir_ircomments = models.TextField(null=True, max_length=2000)
    valid_range_low = models.CharField(null=True, max_length=50)
    valid_range_high = models.CharField(null=True, max_length=50)
    ircommentsvalrange = models.TextField(null=True, max_length=2000)
    par_ircomments = models.TextField(null=True, max_length=2000)
    par_range_low = models.CharField(null=True, max_length=50)
    par_range_high = models.CharField(null=True, max_length=50)
    response_select = models.TextField(null=True, max_length=2000)
    pp_range_select = models.TextField(null=True, max_length=2000)
    ircommentsprop_par = models.TextField(null=True, max_length=2000)

    def __str__(self):
        return self.unitop_text

    class Meta:
        db_table = 'kasaapp_Riskeval'
        unique_together = [("bla_number_id", "unitop_text", "procname_text")]
