from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from .models import unitoperation
from .models import processparameter
from .models import appdata
from .models import riskevaldata
from django.core.mail import send_mail


def home(request):
    if request.method == "POST":
        bla_number = request.POST.get('bla_number')
        searchlist = appdata.objects.filter(bla_number=bla_number)
        return render(request, "kasaapp/home.html", {"appdata": searchlist})

    else:

        return render(request, "kasaapp/home.html", {})


def characterization(request):
    unit = unitoperation.objects.all()
    pps = processparameter.objects.all()
    surrogate = processparameter.objects.exclude(processparameter_name="New process parameter")

    return render(request, "kasaapp/riseval.html",
                  {"unitoperation": unit, "processparameter": pps, "surrogate": surrogate})


def overview(request):
    bla_number = request.POST.get('bla_number')
    applicant_name = request.POST.get('applicant_name')
    application_path = request.POST.get('application_path')
    review = request.POST.get('review')
    proprietary_name = request.POST.get('proprietary_name')
    nonproprietary_name = request.POST.get('nonproprietary_name')
    obp_systematic_name = request.POST.get('obp_systematic_name')
    dosage_form = request.POST.get('dosage_form')
    strength_potency = request.POST.get('strength_potency')
    route_administration = request.POST.get('route_administration')
    primary_assessor = request.POST.get('primary_assessor')
    secondary_assessor = request.POST.get('secondary_assessor')
    drug = request.POST.get('drug')
    review_iteration = request.POST.get('review_iteration')
    reviewer_decision = request.POST.get('reviewer_decision')
    submission_date = request.POST.get('submission_date')
    if not submission_date:
        submission_date = None

    saverecord = appdata(bla_number=bla_number, applicant_name=applicant_name, application_path=application_path, review=review, proprietary_name=proprietary_name, nonproprietary_name=nonproprietary_name, obp_systematic_name=obp_systematic_name, dosage_form=dosage_form, strength_potency=strength_potency, route_administration=route_administration, primary_assessor=primary_assessor, secondary_assessor=secondary_assessor, drug=drug, review_iteration=review_iteration, reviewer_decision=reviewer_decision, submission_date=submission_date)
    saverecord.save()

    return render(request, "kasaapp/overview.html", {"xyz": bla_number})


def riskevaluation(request):
    unit = unitoperation.objects.all()
    pps = processparameter.objects.all()
    surrogate = processparameter.objects.exclude(processparameter_name="New process parameter")
    return render(request, "kasaapp/riskevaluation.html",
                  {"unitoperation": unit, "processparameter": pps, "surrogate": surrogate})



def riskeval(request,pk):
    unit = unitoperation.objects.all()
    pps = processparameter.objects.all()
    surrogate = processparameter.objects.exclude(processparameter_name="New process parameter")

    bla_number_id = pk
    if request.method == 'POST':

        unitop_text = request.POST.get('unitop_text')
        unitop_ircomments = request.POST.get('unitop_ircomments')

        harvest_descriptor = request.POST.get('harvest_descriptor')
        harvest_type_unit = request.POST.get('harvest_type_unit')
        chrom_descr_1 = request.POST.get('chrom_descr_1')
        chrom_descr_1_unit = request.POST.get('chrom_descr_1_unit')
        chrom_descr_2 = request.POST.get('chrom_descr_2')
        chrom_descr_2_unit = request.POST.get('chrom_descr_2_unit')
        chrom_descr_3 = request.POST.get('chrom_descr_3')
        chrom_descr_3_unit = request.POST.get('chrom_descr_3_unit')
        chrom_descr_4 = request.POST.get('chrom_descr_4')
        chrom_descr_4_unit = request.POST.get('chrom_descr_4_unit')
        chrom_descr_5 = request.POST.get('chrom_descr_5')
        chrom_descr_5_unit = request.POST.get('chrom_descr_5_unit')
        chrom_descr_6 = request.POST.get('chrom_descr_6')
        chrom_descr_6_unit = request.POST.get('chrom_descr_6_unit')
        chrom_descr_7 = request.POST.get('chrom_descr_7')
        chrom_descr_7_unit = request.POST.get('chrom_descr_7_unit')
        chrom_descr_8 = request.POST.get('chrom_descr_8')
        chrom_descr_8_unit = request.POST.get('chrom_descr_8')
        chrom_descr_9 = request.POST.get('chrom_descr_9')
        chrom_descr_9_unit = request.POST.get('chrom_descr_9_unit')
        new_descriptor = request.POST.get('new_descriptor')
        newdescriptor_unit = request.POST.get('newdescriptor_unit')
        uf_df_membrane_type = request.POST.get('uf_df_membrane_type')
        membrane_unit = request.POST.get('membrane_unit')
        uf_df_mht = request.POST.get('uf_df_mht')
        micro_holdtime_unit = request.POST.get('micro_holdtime_unit')
        uf_df_bht = request.POST.get('uf_df_bht')
        biochem_holdtime_unit = request.POST.get('biochem_holdtime_unit')
        uf_df_ipt = request.POST.get('uf_df_ipt')
        inprocess_unit = request.POST.get('inprocess_unit')
        thaw_celltype = request.POST.get('thaw_celltype')
        celltype_unit = request.POST.get('celltype_unit')
        thaw_vessel_type = request.POST.get('thaw_vessel_type')
        vessel_unit = request.POST.get('vessel_unit')
        thaw_expansion_type = request.POST.get('thaw_expansion_type')
        expansion_unit = request.POST.get('expansion_unit')
        thaw_ipt = request.POST.get('thaw_ipt')
        inprocess_thaw_unit = request.POST.get('inprocess_thaw_unit')
        prodbio_media_type = request.POST.get('prodbio_media_type')
        media_type_unit = request.POST.get('media_type_unit')
        prodbio_vessel_volume = request.POST.get('prodbio_vessel_volume')
        vessel_volume_unit = request.POST.get('vessel_volume_unit')
        prodbio_composition = request.POST.get('prodbio_composition')
        composition_unit = request.POST.get('composition_unit')
        prodbio_ipt = request.POST.get('prodbio_ipt')
        prodbioinprocess_unit = request.POST.get('prodbioinprocess_unit')
        lowph_acid = request.POST.get('lowph_acid')
        acid_unit = request.POST.get('lowph_acid')
        lowph_base = request.POST.get('lowph_base')
        base_unit = request.POST.get('base_unit')
        lowph_mht = request.POST.get('lowph_mht')
        micro_holdtime_lowph_unit = request.POST.get('micro_holdtime_lowph_unit')
        lowph_bht = request.POST.get('lowph_bht')
        biochem_holdtime_lowph_unit = request.POST.get('biochem_holdtime_lowph_unit')
        lowph_ipt = request.POST.get('lowph_ipt')
        inprocess_lowph_unit = request.POST.get('inprocess_lowph_unit')
        detergent_type = request.POST.get('detergent_type')
        detergent_unit = request.POST.get('detergent_unit')
        detergent_mht = request.POST.get('detergent_mht')
        micro_holdtime_det_unit = request.POST.get('micro_holdtime_det_unit')
        detergent_bht = request.POST.get('detergent_bht')
        biochem_holdtime_det_unit = request.POST.get('biochem_holdtime_det_unit')
        detergent_ipt = request.POST.get('detergent_ipt')
        inprocess_det_unit = request.POST.get('inprocess_det_unit')
        fil_filter = request.POST.get('fil_filter')
        filter_unit = request.POST.get('filter_unit')
        fil_filter_type = request.POST.get('fil_filter_type')
        fil_filter_unit = request.POST.get('fil_filter_unit')
        fil_ipt = request.POST.get('fil_ipt')
        inprocess_viral_unit = request.POST.get('inprocess_viral_unit')
        seedbio_comp = request.POST.get('seedbio_comp')
        seed_bio_composition_unit = request.POST.get('seed_bio_composition_unit')
        seedbio_mediatype = request.POST.get('seedbio_mediatype')
        seedbio_media_unit = request.POST.get('seedbio_media_unit')
        seedbio_ipt = request.POST.get('seedbio_ipt')
        seedbio_inprocess_unit = request.POST.get('seedbio_inprocess_unit')
        procname_text = request.POST.get('procname_text')
        procir_ircomments = request.POST.get('procir_ircomments')
        new_parameter = request.POST.get('new_parameter')
        ircomments_newproc = request.POST.get('ircomments_newproc')
        OBP = request.POST.get('OBP')
        obprisk_ircomments = request.POST.get('obprisk_ircomments')
        applicant_risk_ranking = request.POST.get('applicant_risk_ranking')
        ircomments_apprisk = request.POST.get('ircomments_apprisk')
        applicant_risktext = request.POST.get('applicant_risktext')
        Assign_Risk = request.POST.get('Assign_Risk')
        CPP_KPP = request.POST.get('CPP_KPP')
        cpp_ircomments  = request.POST.get('cpp_ircomments')
        applicant_risk2 = request.POST.get('applicant_risk2')
        surr_applicant_risk_ranking = request.POST.get('surr_applicant_risk_ranking')
        ircomments_surrir = request.POST.get('ircomments_surrir')
        surprocessparameter = request.POST.get('surprocessparameter')
        surrproc_ircomments = request.POST.get('surrproc_ircomments')
        app_sur = request.POST.get('app_sur')
        ircomments_surrapp_risk = request.POST.get('ircomments_surrapp_risk')
        surriskselect = request.POST.get('surriskselect')
        risk_comment = request.POST.get('risk_comment')
        surrisk_text = request.POST.get('surrisk_text')
        surr_Assign_Risk = request.POST.get('surr_Assign_Risk')
        surrCPP_surrKPP = request.POST.get('surrCPP_surrKPP')
        ircomments_surrcpp = request.POST.get('ircomments_surrcpp')
        surrisk_text2 = request.POST.get('surrisk_text2')
        cppdropdownselect = request.POST.get('cppdropdownselect')
        characir_comments = request.POST.get('characir_comments')
        study_appropriate_select = request.POST.get('study_appropriate_select')
        appro_charac_ircomments = request.POST.get('appro_charac_ircomments')
        characterization_study_pk = request.POST.get('characterization_study_pk')
        pk_ircomments = request.POST.get('characterization_study_pk')
        charac_range_low = request.POST.get('charac_range_low')
        charac_range_high = request.POST.get('charac_range_high')
        charac_range_ircomments = request.POST.get('charac_range_ircomments')
        validation_select = request.POST.get('validation_select')
        prelir_ircomments = request.POST.get('prelir_ircomments')
        valid_range_low = request.POST.get('valid_range_low')
        valid_range_high = request.POST.get('valid_range_high')
        ircommentsvalrange = request.POST.get('ircommentsvalrange')
        par_ircomments = request.POST.get('par_ircomments')
        par_range_low = request.POST.get('par_range_low')
        par_range_high = request.POST.get('par_range_high')
        response_select = request.POST.get('response_select')
        pp_range_select = request.POST.get('pp_range_select')
        ircommentsprop_par = request.POST.get('ircommentsprop_par')

        x = riskevaldata.objects.filter(bla_number_id=bla_number_id, unitop_text=unitop_text, procname_text=procname_text)
        if len(x) == 0:
            saverecord = riskevaldata(bla_number_id=bla_number_id, unitop_text=unitop_text, harvest_descriptor=harvest_descriptor, harvest_type_unit=harvest_type_unit, chrom_descr_1=chrom_descr_1, chrom_descr_1_unit=chrom_descr_1_unit, chrom_descr_2=chrom_descr_2, chrom_descr_2_unit=chrom_descr_2_unit,
             chrom_descr_3=chrom_descr_3, chrom_descr_3_unit=chrom_descr_3_unit,chrom_descr_4=chrom_descr_4, chrom_descr_4_unit=chrom_descr_4_unit, chrom_descr_5=chrom_descr_5, chrom_descr_5_unit=chrom_descr_5_unit, chrom_descr_6=chrom_descr_6, chrom_descr_6_unit=chrom_descr_6_unit, chrom_descr_7=chrom_descr_7, chrom_descr_7_unit=chrom_descr_7_unit,
             chrom_descr_8=chrom_descr_8, chrom_descr_8_unit=chrom_descr_8_unit, chrom_descr_9=chrom_descr_9,chrom_descr_9_unit=chrom_descr_9_unit, new_descriptor=new_descriptor, newdescriptor_unit=newdescriptor_unit, uf_df_membrane_type=uf_df_membrane_type, membrane_unit=membrane_unit, uf_df_mht=uf_df_mht, micro_holdtime_unit=micro_holdtime_unit, uf_df_bht=uf_df_bht, biochem_holdtime_unit=biochem_holdtime_unit,
             uf_df_ipt=uf_df_ipt, inprocess_unit=inprocess_unit, thaw_celltype=thaw_celltype, celltype_unit=celltype_unit, thaw_vessel_type=thaw_vessel_type, vessel_unit=vessel_unit, thaw_expansion_type=thaw_expansion_type, expansion_unit=expansion_unit, thaw_ipt=thaw_ipt, inprocess_thaw_unit=inprocess_thaw_unit, prodbio_media_type=prodbio_media_type, media_type_unit=media_type_unit, prodbio_vessel_volume=prodbio_vessel_volume,
             vessel_volume_unit=vessel_volume_unit, prodbio_composition=prodbio_composition, composition_unit=composition_unit, prodbio_ipt=prodbio_ipt, prodbioinprocess_unit=prodbioinprocess_unit, lowph_acid=lowph_acid, acid_unit=acid_unit, lowph_base=lowph_base, base_unit=base_unit, lowph_mht=lowph_mht, micro_holdtime_lowph_unit=micro_holdtime_lowph_unit, lowph_bht=lowph_bht, biochem_holdtime_lowph_unit=biochem_holdtime_lowph_unit, lowph_ipt=lowph_ipt,
             inprocess_lowph_unit=inprocess_lowph_unit, detergent_type=detergent_type, detergent_unit=detergent_unit, detergent_mht=detergent_mht, micro_holdtime_det_unit=micro_holdtime_det_unit, detergent_bht=detergent_bht, biochem_holdtime_det_unit=biochem_holdtime_det_unit, detergent_ipt=detergent_ipt, inprocess_det_unit=inprocess_det_unit, fil_filter=fil_filter, filter_unit=filter_unit, fil_filter_type=fil_filter_type, fil_filter_unit=fil_filter_unit,
             fil_ipt=fil_ipt, inprocess_viral_unit=inprocess_viral_unit, seedbio_comp=seedbio_comp, seed_bio_composition_unit=seed_bio_composition_unit,seedbio_mediatype=seedbio_mediatype, seedbio_media_unit=seedbio_media_unit, seedbio_ipt=seedbio_ipt, seedbio_inprocess_unit=seedbio_inprocess_unit,
             procname_text=procname_text, new_parameter=new_parameter, OBP=OBP, applicant_risk_ranking=applicant_risk_ranking, applicant_risktext=applicant_risktext, Assign_Risk=Assign_Risk, CPP_KPP=CPP_KPP, applicant_risk2=applicant_risk2, surr_applicant_risk_ranking=surr_applicant_risk_ranking, surprocessparameter=surprocessparameter, app_sur=app_sur, surriskselect=surriskselect,
             risk_comment=risk_comment, surrisk_text=surrisk_text, surr_Assign_Risk=surr_Assign_Risk, surrCPP_surrKPP=surrCPP_surrKPP, surrisk_text2=surrisk_text2, unitop_ircomments=unitop_ircomments, procir_ircomments=procir_ircomments, ircomments_newproc=ircomments_newproc,ircomments_surrir=ircomments_surrir, surrproc_ircomments=surrproc_ircomments, ircomments_apprisk=ircomments_apprisk, obprisk_ircomments=obprisk_ircomments, ircomments_surrapp_risk=ircomments_surrapp_risk, cpp_ircomments=cpp_ircomments, ircomments_surrcpp=ircomments_surrcpp, cppdropdownselect=cppdropdownselect, characir_comments=characir_comments,study_appropriate_select=study_appropriate_select,
             appro_charac_ircomments=appro_charac_ircomments, characterization_study_pk=characterization_study_pk, pk_ircomments=pk_ircomments, charac_range_low=charac_range_low, charac_range_high=charac_range_high,charac_range_ircomments=charac_range_ircomments, validation_select=validation_select, prelir_ircomments=prelir_ircomments, valid_range_low=valid_range_low, valid_range_high=valid_range_high, ircommentsvalrange=ircommentsvalrange, par_ircomments=par_ircomments, par_range_low=par_range_low,par_range_high=par_range_high,response_select=response_select, pp_range_select=pp_range_select, ircommentsprop_par=ircommentsprop_par)

            saverecord.save()
        else:
            y = x[0]
            y.harvest_type_unit = harvest_type_unit
            y.chrom_descr_1 = chrom_descr_1
            y.chrom_descr_1_unit = chrom_descr_1_unit
            y.chrom_descr_2 = chrom_descr_2
            y.chrom_descr_2_unit = chrom_descr_2_unit
            y.chrom_descr_3 = chrom_descr_3
            y.chrom_descr_3_unit = chrom_descr_3_unit
            y.chrom_descr_4 = chrom_descr_4
            y.chrom_descr_4_unit = chrom_descr_4_unit
            y.chrom_descr_5 = chrom_descr_5
            y.chrom_descr_5_unit = chrom_descr_5_unit
            y.chrom_descr_6 = chrom_descr_6
            y.chrom_descr_6_unit = chrom_descr_6_unit
            y.chrom_descr_7 = chrom_descr_7
            y.chrom_descr_7_unit = chrom_descr_7_unit
            y.chrom_descr_8 = chrom_descr_8
            y.chrom_descr_8_unit = chrom_descr_8_unit
            y.chrom_descr_9 = chrom_descr_9
            y.chrom_descr_9_unit = chrom_descr_9_unit
            y.new_descriptor = new_descriptor
            y.newdescriptor_unit = newdescriptor_unit
            y.uf_df_membrane_type = uf_df_membrane_type
            y.membrane_unit = membrane_unit
            y.uf_df_mht = uf_df_mht
            y.micro_holdtime_unit = micro_holdtime_unit
            y.uf_df_bht = uf_df_bht
            y.biochem_holdtime_unit = biochem_holdtime_unit
            y.uf_df_ipt = uf_df_ipt
            y.inprocess_unit = inprocess_unit
            y.thaw_celltype = thaw_celltype
            y.celltype_unit = celltype_unit
            y.thaw_vessel_type = thaw_vessel_type
            y.vessel_unit = vessel_unit
            y.thaw_expansion_type = thaw_expansion_type
            y.expansion_unit = expansion_unit
            y.thaw_ipt = thaw_ipt
            y.inprocess_thaw_unit = inprocess_thaw_unit
            y.prodbio_media_type = prodbio_media_type
            y.media_type_unit = media_type_unit
            y.prodbio_vessel_volume = prodbio_vessel_volume
            y.vessel_volume_unit = vessel_volume_unit
            y.prodbio_composition = prodbio_composition
            y.composition_unit = composition_unit
            y.prodbio_ipt = prodbio_ipt
            y.prodbioinprocess_unit = prodbioinprocess_unit
            y.lowph_acid = lowph_acid
            y.acid_unit = acid_unit
            y.lowph_base = lowph_base
            y.base_unit = base_unit
            y.lowph_mht = lowph_mht
            y.micro_holdtime_lowph_unit = micro_holdtime_lowph_unit
            y.lowph_bht = lowph_bht
            y.biochem_holdtime_lowph_unit = biochem_holdtime_lowph_unit
            y.lowph_ipt = lowph_ipt
            y.inprocess_lowph_unit = inprocess_lowph_unit
            y.detergent_type = detergent_type
            y.detergent_unit = detergent_unit
            y.detergent_mht = detergent_mht
            y.micro_holdtime_det_unit = micro_holdtime_det_unit
            y.detergent_bht = detergent_bht
            y.biochem_holdtime_det_unit = biochem_holdtime_det_unit
            y.detergent_ipt = detergent_ipt
            y.inprocess_det_unit = inprocess_det_unit
            y.fil_filter = fil_filter
            y.filter_unit = filter_unit
            y.fil_filter_type = fil_filter_type
            y.fil_filter_unit = fil_filter_unit
            y.fil_ipt = fil_ipt
            y.inprocess_viral_unit = inprocess_viral_unit
            y.seedbio_comp = seedbio_comp
            y.seed_bio_composition_unit = seed_bio_composition_unit
            y.seedbio_mediatype = seedbio_mediatype
            y.seedbio_media_unit = seedbio_media_unit
            y.seedbio_ipt = seedbio_ipt
            y.seedbio_inprocess_unit = seedbio_inprocess_unit
            y.new_parameter = new_parameter
            y.OBP = OBP
            y.applicant_risk_ranking = applicant_risk_ranking
            y.applicant_risktext = applicant_risktext
            y.Assign_Risk = Assign_Risk
            y.CPP_KPP = CPP_KPP
            y.applicant_risk2 = applicant_risk2
            y.surr_applicant_risk_ranking = surr_applicant_risk_ranking
            y.surprocessparameter = surprocessparameter
            y.app_sur = app_sur
            y.surriskselect = surriskselect
            y.risk_comment = risk_comment
            y.surrisk_text = surrisk_text
            y.surr_Assign_Risk = surr_Assign_Risk
            y.surrCPP_surrKPP = surrCPP_surrKPP
            y.surrisk_text2 = surrisk_text2
            y.unitop_ircomments = unitop_ircomments
            y.procir_ircomments = procir_ircomments
            y.ircomments_newproc = ircomments_newproc
            y.ircomments_surrir = ircomments_surrir
            y.surrproc_ircomments= surrproc_ircomments
            y.ircomments_apprisk = ircomments_apprisk
            y.obprisk_ircomments = obprisk_ircomments
            y.ircomments_surrapp_risk = ircomments_surrapp_risk
            y.cpp_ircomments = cpp_ircomments
            y.ircomments_surrcpp = ircomments_surrcpp
            y.cppdropdownselect = cppdropdownselect
            y.cpp_ircomments = cpp_ircomments
            y.study_appropriate_select =study_appropriate_select
            y.appro_charac_ircomments= appro_charac_ircomments
            y.characterization_study_pk = characterization_study_pk
            y.pk_ircomments = pk_ircomments
            y.pk_ircomments = pk_ircomments
            y.charac_range_low = charac_range_low
            y.charac_range_high = charac_range_high
            y.charac_range_ircomments = charac_range_ircomments
            y.validation_select = validation_select
            y.prelir_ircomments = prelir_ircomments
            y.valid_range_low = valid_range_low
            y.valid_range_high = valid_range_high
            y.ircommentsvalrange = ircommentsvalrange
            y.par_ircomments = par_ircomments
            y.par_range_low = par_range_low
            y.par_range_high = par_range_high
            y.response_select = response_select
            y.pp_range_select = pp_range_select
            y.ircommentsprop_par = ircommentsprop_par

            y.save()



        return render(request,"kasaapp/riskeval.html",
                      {"xyz": bla_number_id,  "unitoperation": unit, "processparameter": pps, "surrogate": surrogate})
    else:
        return render(request, "kasaapp/riskeval.html",
                      {"xyz": bla_number_id, "unitoperation": unit, "processparameter": pps, "surrogate": surrogate})


def summary(request):
    unitop_text = request.POST.get('unitop_text', None)
    chrom_descr_1 = request.POST.get('chrom_descr_1', None)
    chrom_descr_2 = request.POST.get('chrom_descr_2', None)
    chrom_descr_3 = request.POST.get('chrom_descr_3', None)
    chrom_descr_4 = request.POST.get('chrom_descr_4', None)
    chrom_descr_5 = request.POST.get('chrom_descr_5', None)
    chrom_descr_6 = request.POST.get('chrom_descr_6', None)
    chrom_descr_7 = request.POST.get('chrom_descr_7', None)
    chrom_descr_8 = request.POST.get('chrom_descr_8', None)
    chrom_descr_9 = request.POST.get('chrom_descr_9', None)
    new_parameter = request.POST.get('new_parameter', None)
    new_proc_comment = request.POST.get('new_proc_comment', None)
    surr_comment = request.POST.get('surr_comment', None)
    app_risk = request.POST.get('app_risk', None)
    surr_pp_comment = request.POST.get('surr_pp_comment', None)
    obp_risk_comment = request.POST.get('obp_risk_comment', None)
    app_risk_surr_comment = request.POST.get('app_risk_surr_comment', None)
    na_risk_comment = request.POST.get('na_risk_comment', None)
    risk_comment = request.POST.get('risk_comment', None)
    surr_risk_comment2 = request.POST.get('surr_risk_comment2', None)
    surr_ranking_comment = request.POST.get('surr_ranking_comment', None)
    surr_risk_comment = request.POST.get('surr_risk_comment', None)
    proc_comment = request.POST.get('proc_comment', None)
    CPPKPP_comment = request.POST.get('CPPKPP_comment', None)
    surr_CPPKPP_comment = request.POST.get('surr_CPPKPP_comment', None)
    ircomments = request.POST.get('ircomments', None)
    charac_range_low = request.POST.get('charac_range_low', None)
    charac_range_high = request.POST.get('charac_range_high', None)
    valid_range_low = request.POST.get('valid_range_low', None)
    valid_range_high = request.POST.get('valid_range_high', None)
    par_range_low = request.POST.get('par_range_low', None)
    par_range_high = request.POST.get('par_range_high', None)
    harvest_descriptor = request.POST.get('harvest_descriptor', None)
    harvest_type_unit = request.POST.get('harvest_type_unit', None)
    uf_df_membrane_type = request.POST.get('uf_df_membrane_type', None)
    membrane_unit = request.POST.get('membrane_unit', None)
    uf_df_mht = request.POST.get('uf_df_mht', None)
    micro_holdtime_unit = request.POST.get('micro_holdtime_unit', None)
    uf_df_bht = request.POST.get('uf_df_bht', None)
    biochem_holdtime_unit = request.POST.get('biochem_holdtime_unit', None)
    uf_df_ipt = request.POST.get('uf_df_ipt', None)
    inprocess_unit = request.POST.get('inprocess_unit', None)
    thaw_celltype = request.POST.get('thaw_celltype', None)
    celltype_unit = request.POST.get('celltype_unit', None)
    thaw_vessel_type = request.POST.get('thaw_vessel_type', None)
    vessel_unit = request.POST.get('vessel_unit', None)
    thaw_expansion_type = request.POST.get('thaw_expansion_type', None)
    expansion_unit = request.POST.get('expansion_unit', None)
    thaw_ipt = request.POST.get('thaw_ipt', None)
    inprocess_thaw_unit = request.POST.get('inprocess_thaw_unit', None)
    prodbio_media_type = request.POST.get('prodbio_media_type', None)
    media_type_unit = request.POST.get('media_type_unit', None)
    prodbio_vessel_volume = request.POST.get('prodbio_vessel_volume', None)
    vessel_volume_unit = request.POST.get('vessel_volume_unit', None)
    prodbio_composition = request.POST.get('prodbio_composition', None)
    composition_unit = request.POST.get('composition_unit', None)
    prodbio_ipt = request.POST.get('prodbio_ipt', None)
    prodbioinprocess_unit = request.POST.get('prodbioinprocess_unit', None)
    lowph_acid = request.POST.get('lowph_acid', None)
    acid_unit = request.POST.get('acid_unit', None)
    lowph_base = request.POST.get('lowph_base', None)
    base_unit = request.POST.get('base_unit', None)
    lowph_mht = request.POST.get('lowph_mht', None)
    lowph_bht = request.POST.get('lowph_bht', None)
    micro_holdtime_lowph_unit = request.POST.get('micro_holdtime_lowph_unit', None)
    biochem_holdtime_lowph_unit = request.POST.get('biochem_holdtime_lowph_unit', None)
    lowph_ipt = request.POST.get('lowph_ipt', None)
    inprocess_lowph_unit = request.POST.get('inprocess_lowph_unit', None)
    detergent_lowph_unit = request.POST.get('detergent_lowph_unit', None)
    detergent_type = request.POST.get('detergent_type', None)
    detergent_mht = request.POST.get('detergent_mht', None)
    micro_holdtime_det_unit = request.POST.get('micro_holdtime_det_unit', None)
    detergent_bht = request.POST.get('detergent_bht', None)
    biochem_holdtime_det_unit = request.POST.get('biochem_holdtime_det_unit', None)
    detergent_ipt = request.POST.get('detergent_ipt', None)
    inprocess_det_unit = request.POST.get('inprocess_det_unit', None)
    fil_filter = request.POST.get('fil_filter', None)
    fil_filter_unit = request.POST.get('fil_filter_unit', None)
    fil_filter_type = request.POST.get('fil_filter_type', None)
    filter_unit = request.POST.get('filter_unit', None)
    fil_ipt = request.POST.get('fil_ipt', None)
    inprocess_viral_unit = request.POST.get('inprocess_viral_unit', None)
    seedbio_comp = request.POST.get('seedbio_comp', None)
    seedbio_composition_unit = request.POST.get('seedbio_composition_unit', None)
    seedbio_mediatype = request.POST.get('seedbio_mediatype', None)
    seedbio_media_unit = request.POST.get('seedbio_media_unit', None)
    seedbio_ipt = request.POST.get('seedbio_ipt', None)
    seedbio_inprocess_unit = request.POST.get('seedbio_inprocess_unit', None)
    unitop_ircomments = request.POST.get('unitop_ircomments', None)
    procir_ircomments = request.POST.get('procir_ircomments', None)
    apprisk_ircomments = request.POST.get('apprisk_ircomments', None)
    characir_comments = request.POST.get('characir_comments', None)
    appro_charac_ircomments = request.POST.get('appro_charac_ircomments', None)
    charac_range_ircomments = request.POST.get('charac_range_ircomments', None)
    val_ircomments = request.POST.get('val_ircomments', None)
    valrange_ircomments = request.POST.get('valrange_ircomments', None)
    par_ircomments = request.POST.get('par_ircomments', None)
    prop_par_ircomments = request.POST.get('prop_par_ircomments', None)
    obprisk_ircomments = request.POST.get('obprisk_ircomments', None)
    procname_text = request.POST.get('procname_text', None)
    applicantrisk = request.POST.get('applicant_risktext', None)
    applicantrisk2 = request.POST.get('applicant_risk2', None)
    surprocessparameter = request.POST.get('surprocessparameter', '--Select Process Parameter--')
    surrisk = request.POST.get('surrisk_text', None)
    surrisk2 = request.POST.get('surrisk_text2', None)

    return render(request, "kasaapp/summary.html", {"unitoperationname": unitop_text,
                                                    "Chromatography_descriptor1": chrom_descr_1,
                                                    "Chromatography_descriptor2": chrom_descr_2,
                                                    "Chromatography_descriptor3": chrom_descr_3,
                                                    "Chromatography_descriptor4": chrom_descr_4,
                                                    "Chromatography_descriptor5": chrom_descr_5,
                                                    "Chromatography_descriptor6": chrom_descr_6,
                                                    "Chromatography_descriptor7": chrom_descr_7,
                                                    "Chromatography_descriptor8": chrom_descr_8,
                                                    "Chromatography_descriptor9": chrom_descr_9,
                                                    "newprocessparameter": new_parameter,
                                                    "new_proc_comment": new_proc_comment,
                                                    "surr_comment": surr_comment,
                                                    "surr_pp_comment": surr_pp_comment,
                                                    "app_risk": app_risk,
                                                    "obp_risk_comment": obp_risk_comment,
                                                    "app_risk_surr_comment": app_risk_surr_comment,
                                                    "na_risk_comment": na_risk_comment,
                                                    "risk_comment": risk_comment,
                                                    "surr_ranking_comment": surr_ranking_comment,
                                                    "surr_risk_comment2": surr_risk_comment2,
                                                    "surr_risk_comment": surr_risk_comment,
                                                    "proc_comment": proc_comment,
                                                    "CPP/KPP_comment": CPPKPP_comment,
                                                    "surr_CPPKPP_comment": surr_CPPKPP_comment,
                                                    "ircomments": ircomments,
                                                    "procname_text": procname_text,
                                                    "charac_range_low": charac_range_low,
                                                    "charac_range_high": charac_range_high,
                                                    "valid_range_high": valid_range_high,
                                                    "valid_range_low": valid_range_low,
                                                    "par_range_high": par_range_high,
                                                    "harvest_descriptor": harvest_descriptor,
                                                    "harvest_type_unit": harvest_type_unit,
                                                    "uf_df_membrane_type": uf_df_membrane_type,
                                                    "membrane_unit": membrane_unit,
                                                    "uf_df_mht": uf_df_mht,
                                                    "micro_holdtime_unit": micro_holdtime_unit,
                                                    "uf_df_bht": uf_df_bht,
                                                    "biochem_holdtime_unit": biochem_holdtime_unit,
                                                    "uf_df_ipt": uf_df_ipt,
                                                    "inprocess_unit": inprocess_unit,
                                                    "thaw_celltype": thaw_celltype,
                                                    "celltype_unit": celltype_unit,
                                                    "thaw_vessel_type": thaw_vessel_type,
                                                    "vessel_unit": vessel_unit,
                                                    "thaw_expansion_type": thaw_expansion_type,
                                                    "expansion_unit": expansion_unit,
                                                    "thaw_ipt": thaw_ipt,
                                                    "inprocess_thaw_unit": inprocess_thaw_unit,
                                                    "prodbio_media_type": prodbio_media_type,
                                                    "media_type_unit": media_type_unit,
                                                    "prodbio_vessel_volume": prodbio_vessel_volume,
                                                    "vessel_volume_unit": vessel_volume_unit,
                                                    "prodbio_composition": prodbio_composition,
                                                    "composition_unit": composition_unit,
                                                    "prodbio_ipt": prodbio_ipt,
                                                    "prodbioinprocess_unit": prodbioinprocess_unit,
                                                    "lowph_acid": lowph_acid,
                                                    "acid_unit": acid_unit,
                                                    "lowph_base": lowph_base,
                                                    "base_unit": base_unit,
                                                    "lowph_mht": lowph_mht,
                                                    "micro_holdtime_lowph_unit": micro_holdtime_lowph_unit,
                                                    "lowph_bht": lowph_bht,
                                                    "biochem_holdtime_lowph_unit": biochem_holdtime_lowph_unit,
                                                    "lowph_ipt": lowph_ipt,
                                                    "inprocess_lowph_unit": inprocess_lowph_unit,
                                                    "detergent_type": detergent_type,
                                                    "detergent_lowph_unit": detergent_lowph_unit,
                                                    "detergent_mht": detergent_mht,
                                                    "micro_holdtime_det_unit": micro_holdtime_det_unit,
                                                    "detergent_bht": detergent_bht,
                                                    "biochem_holdtime_det_unit": biochem_holdtime_det_unit,
                                                    "detergent_ipt": detergent_ipt,
                                                    "inprocess_det_unit": inprocess_det_unit,
                                                    "fil_filter": fil_filter,
                                                    "fil_filter_unit": fil_filter_unit,
                                                    "filter_unit": filter_unit,
                                                    "fil_ipt": fil_ipt,
                                                    "inprocess_viral_unit": inprocess_viral_unit,
                                                    "seedbio_comp": seedbio_comp,
                                                    "seedbio_composition_unit": seedbio_composition_unit,
                                                    "seedbio_mediatype": seedbio_mediatype,
                                                    "seedbio_media_unit": seedbio_media_unit,
                                                    "seedbio_ipt": seedbio_ipt,
                                                    "seedbio_inprocess_unit": seedbio_inprocess_unit,
                                                    "fil_filter_type": fil_filter_type,
                                                    "par_range_low": par_range_low,
                                                    "unitop_ircomments": unitop_ircomments,
                                                    "procir_ircomments": procir_ircomments,
                                                    "apprisk_ircomments": apprisk_ircomments,
                                                    "obprisk_ircomments": obprisk_ircomments,
                                                    "characir_comments": characir_comments,
                                                    "appro_charac_ircomments": appro_charac_ircomments,
                                                    "charac_range_ircomments": charac_range_ircomments,
                                                    "val_ircomments": val_ircomments,
                                                    "valrange_ircomments": valrange_ircomments,
                                                    "par_ircomments": par_ircomments,
                                                    "prop_par_ircomments": prop_par_ircomments,
                                                    "preliminaryrisk": applicantrisk,
                                                    "preliminaryrisk1": applicantrisk2,
                                                    "surprocessparametername": surprocessparameter,
                                                    "surpreliminaryrisk": surrisk,
                                                    "surpreliminaryrisk2": surrisk2
                                                    })


