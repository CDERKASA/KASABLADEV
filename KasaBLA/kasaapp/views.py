from django.http import HttpResponse
from django.shortcuts import render
from .models import unitoperation
from .models import processparameter
from .models import Overview
from .models import Riskeval
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse
import json


def home(request):
    query = None
    results = []
    if request.method == "POST":
        query = request.POST.POST('search')
        if query:
            results = Overview.objects.filter(Q(bla_number=query))
    return render(request, "kasaapp/home.html", {'query': query, 'results': results})


def characterization(request):
    processparam = processparameter.objects.all()
    unitops = unitoperation.objects.all()
    return render(request, "kasaapp/characterization.html",
                  {"unit": unitops, "pp": processparam})


def overview(request):
    overview_page = Overview.objects.all()
    response_data = {}

    if request.POST.POST('action') == 'POST':
        application_path = request.POST.POST('application_path')
        applicant_name = request.POST.POST('applicant_name')
        bla_number = request.POST.POST('bla_number')
        review = request.POST.POST('review')
        review_iteration = request.POST.POST('review_iteration')
        review_decision = request.POST.POST('review_decision')
        designation = request.POST.POST('designation')
        prop_name = request.POST.POST('prop_name')
        non_prop_name = request.POST.POST('non_prop_name')
        obp_name = request.POST.POST('obp_name')
        dosage_form = request.POST.POST('dosage_form')
        strength_potency = request.POST.POST('strength_potency')
        route_administration = request.POST.POST('route_administration')
        primary_assessor = request.POST.POST('primary_assessor')
        secondary_assessor = request.POST.POST('secondary_assessor')

        response_data['application_path'] = application_path
        response_data['applicant_name'] = applicant_name
        response_data['bla_number'] = bla_number
        response_data['review'] = review
        response_data['review_iteration'] = review_iteration
        response_data['review_decision'] = review_decision
        response_data['designation'] = designation
        response_data['prop_name'] = prop_name
        response_data['non_prop_name'] = non_prop_name
        response_data['obp_name'] = obp_name
        response_data['dosage_form'] = dosage_form
        response_data['strength_potency'] = strength_potency
        response_data['route_administration'] = route_administration
        response_data['primary_assessor'] = primary_assessor
        response_data['secondary_assessor'] = secondary_assessor

        ins = Overview(application_path=application_path, bla_number=bla_number,
                       applicant_name=applicant_name, prop_name=prop_name, non_prop_name=non_prop_name,
                       obp_name=obp_name, dosage_form=dosage_form, strength_potency=strength_potency,
                       route_administration=route_administration, primary_assessor=primary_assessor,
                       secondary_assessor=secondary_assessor, review=review, designation=designation,
                       review_iteration=review_iteration, review_decision=review_decision)
        ins.save()
        return JsonResponse(response_data)

    return render(request, "kasaapp/overview.html", {"overview_page": overview_page})


def riskeval(request):
    riskeval_page = Riskeval.objects.all()
    response_data = {}
    unit = unitoperation.objects.all()
    pps = processparameter.objects.all()
    surrogate = processparameter.objects.exclude(processparameter_name="New process parameter")

    if request.POST.POST('action') == 'POST':
        unitop_text = request.POST.POST('unitop_text')
        unitop_ircomments = request.POST.POST('unitop_ircomments')
        harvest_descriptor = request.POST.POST('harvest_descriptor')
        harvest_type_unit = request.POST.POST('harvest_type_unit')
        chrom_descr_1 = request.POST.POST('chrom_descr_1')
        chrom_descr_1_unit = request.POST.POST('chrom_descr_1_unit')
        chrom_descr_2 = request.POST.POST('chrom_descr_2')
        chrom_descr_2_unit = request.POST.POST('chrom_descr_2_unit')
        chrom_descr_3 = request.POST.POST('chrom_descr_3')
        chrom_descr_3_unit = request.POST.POST('chrom_descr_3_unit')
        chrom_descr_4 = request.POST.POST('chrom_descr_4')
        chrom_descr_4_unit = request.POST.POST('chrom_descr_4_unit')
        chrom_descr_5 = request.POST.POST('chrom_descr_5')
        chrom_descr_5_unit = request.POST.POST('chrom_descr_5_unit')
        chrom_descr_6 = request.POST.POST('chrom_descr_6')
        chrom_descr_6_unit = request.POST.POST('chrom_descr_6_unit')
        chrom_descr_7 = request.POST.POST('chrom_descr_7')
        chrom_descr_7_unit = request.POST.POST('chrom_descr_7_unit')
        chrom_descr_8 = request.POST.POST('chrom_descr_8')
        chrom_descr_8_unit = request.POST.POST('chrom_descr_8_unit')
        chrom_descr_9 = request.POST.POST('chrom_descr_9')
        chrom_descr_9_unit = request.POST.POST('chrom_descr_9_unit')
        new_descriptor = request.POST.POST('new_descriptor')
        newdescriptor_unit = request.POST.POST('newdescriptor_unit')
        uf_df_membrane_type = request.POST.POST('uf_df_membrane_type')
        membrane_unit = request.POST.POST('membrane_unit')
        uf_df_mht = request.POST.POST('uf_df_mht')
        micro_holdtime_unit = request.POST.POST('micro_holdtime_unit')
        uf_df_bht = request.POST.POST('uf_df_bht')
        biochem_holdtime_unit = request.POST.POST('biochem_holdtime_unit')
        uf_df_ipt = request.POST.POST('uf_df_ipt')
        inprocess_unit = request.POST.POST('inprocess_unit')
        thaw_celltype = request.POST.POST('thaw_celltype')
        celltype_unit = request.POST.POST('celltype_unit')
        thaw_vessel_type = request.POST.POST('thaw_vessel_type')
        vessel_unit = request.POST.POST('vessel_unit')
        thaw_expansion_type = request.POST.POST('thaw_expansion_type')
        expansion_unit = request.POST.POST('expansion_unit')
        thaw_ipt = request.POST.POST('thaw_ipt')
        inprocess_thaw_unit = request.POST.POST('inprocess_thaw_unit')
        prodbio_media_type = request.POST.POST('prodbio_media_type')
        media_type_unit = request.POST.POST('media_type_unit')
        prodbio_vessel_volume = request.POST.POST('prodbio_vessel_volume')
        vessel_volume_unit = request.POST.POST('vessel_volume_unit')
        prodbio_composition = request.POST.POST('prodbio_composition')
        composition_unit = request.POST.POST('composition_unit')
        prodbio_ipt = request.POST.POST('prodbio_ipt')
        prodbioinprocess_unit = request.POST.POST('prodbioinprocess_unit')
        lowph_acid = request.POST.POST('lowph_acid')
        acid_unit = request.POST.POST('lowph_acid')
        lowph_base = request.POST.POST('lowph_base')
        base_unit = request.POST.POST('base_unit')
        lowph_mht = request.POST.POST('lowph_mht')
        micro_holdtime_lowph_unit = request.POST.POST('micro_holdtime_lowph_unit')
        lowph_bht = request.POST.POST('lowph_bht')
        biochem_holdtime_lowph_unit = request.POST.POST('biochem_holdtime_lowph_unit')
        lowph_ipt = request.POST.POST('lowph_ipt')
        inprocess_lowph_unit = request.POST.POST('inprocess_lowph_unit')
        detergent_type = request.POST.POST('detergent_type')
        detergent_unit = request.POST.POST('detergent_unit')
        detergent_mht = request.POST.POST('detergent_mht')
        micro_holdtime_det_unit = request.POST.POST('micro_holdtime_det_unit')
        detergent_bht = request.POST.POST('detergent_bht')
        biochem_holdtime_det_unit = request.POST.POST('biochem_holdtime_det_unit')
        detergent_ipt = request.POST.POST('detergent_ipt')
        inprocess_det_unit = request.POST.POST('inprocess_det_unit')
        fil_filter = request.POST.POST('fil_filter')
        filter_unit = request.POST.POST('filter_unit')
        fil_filter_type = request.POST.POST('fil_filter_type')
        fil_filter_unit = request.POST.POST('fil_filter_unit')
        fil_ipt = request.POST.POST('fil_ipt')
        inprocess_viral_unit = request.POST.POST('inprocess_viral_unit')
        seedbio_comp = request.POST.POST('seedbio_comp')
        seed_bio_composition_unit = request.POST.POST('seed_bio_composition_unit')
        seedbio_mediatype = request.POST.POST('seedbio_mediatype')
        seedbio_media_unit = request.POST.POST('seedbio_media_unit')
        seedbio_ipt = request.POST.POST('seedbio_ipt')
        seedbio_inprocess_unit = request.POST.POST('seedbio_inprocess_unit')
        procname_text = request.POST.POST('procname_text')
        procir_ircomments = request.POST.POST('procir_ircomments')
        new_parameter = request.POST.POST('new_parameter')
        ircomments_newproc = request.POST.POST('ircomments_newproc')
        OBP = request.POST.POST('OBP')
        obprisk_ircomments = request.POST.POST('obprisk_ircomments')
        applicant_risk_ranking = request.POST.POST('applicant_risk_ranking')
        ircomments_apprisk = request.POST.POST('ircomments_apprisk')
        new_proc_comment = request.POST.POST('new_proc_comment')
        applicant_risktext = request.POST.POST('applicant_risktext')
        Assign_Risk = request.POST.POST('Assign_Risk')
        CPP_KPP = request.POST.POST('CPP_KPP')
        cpp_ircomments = request.POST.POST('cpp_ircomments')
        applicant_risk2 = request.POST.POST('applicant_risk2')
        surr_applicant_risk_ranking = request.POST.POST('surr_applicant_risk_ranking')
        ircomments_surrir = request.POST.POST('ircomments_surrir')
        surprocessparameter = request.POST.POST('surprocessparameter')
        surrproc_ircomments = request.POST.POST('surrproc_ircomments')
        app_sur = request.POST.POST('app_sur')
        ircomments_surrapp_risk = request.POST.POST('ircomments_surrapp_risk')
        surriskselect = request.POST.POST('surriskselect')
        risk_comment = request.POST.POST('risk_comment')
        surrisk_text = request.POST.POST('surrisk_text')
        surr_Assign_Risk = request.POST.POST('surr_Assign_Risk')
        surrCPP_surrKPP = request.POST.POST('surrCPP_surrKPP')
        ircomments_surrcpp = request.POST.POST('ircomments_surrcpp')
        surrisk_text2 = request.POST.POST('surrisk_text2')
        cppdropdownselect = request.POST.POST('cppdropdownselect')
        characir_comments = request.POST.POST('characir_comments')
        study_appropriate_select = request.POST.POST('study_appropriate_select')
        appro_charac_ircomments = request.POST.POST('appro_charac_ircomments')
        characterization_study_pk = request.POST.POST('characterization_study_pk')
        pk_ircomments = request.POST.POST('pk_ircomments')
        charac_range_low = request.POST.POST('charac_range_low')
        charac_range_high = request.POST.POST('charac_range_high')
        charac_range_ircomments = request.POST.POST('charac_range_ircomments')
        validation_select = request.POST.POST('validation_select')
        prelir_ircomments = request.POST.POST('prelir_ircomments')
        valid_range_low = request.POST.POST('valid_range_low')
        valid_range_high = request.POST.POST('valid_range_high')
        ircommentsvalrange = request.POST.POST('ircommentsvalrange')
        par_ircomments = request.POST.POST('par_ircomments')
        par_range_low = request.POST.POST('par_range_low')
        par_range_high = request.POST.POST('par_range_high')
        response_select = request.POST.POST('response_select')
        pp_range_select = request.POST.POST('pp_range_select')
        ircommentsprop_par = request.POST.POST('ircommentsprop_par')

        response_data['unitop_text'] = unitop_text
        response_data['unitop_ircomments'] = unitop_ircomments
        response_data['harvest_descriptor'] = harvest_descriptor
        response_data['harvest_type_unit'] = harvest_type_unit
        response_data['chrom_descr_1'] = chrom_descr_1
        response_data['chrom_descr_1_unit'] = chrom_descr_1_unit
        response_data['chrom_descr_2'] = chrom_descr_2
        response_data['chrom_descr_2_unit'] = chrom_descr_2_unit
        response_data['chrom_descr_3'] = chrom_descr_3
        response_data['chrom_descr_3_unit'] = chrom_descr_3_unit
        response_data['chrom_descr_4'] = chrom_descr_4
        response_data['chrom_descr_4_unit '] = chrom_descr_4_unit
        response_data['chrom_descr_5'] = chrom_descr_5
        response_data['chrom_descr_5_unit'] = chrom_descr_5_unit
        response_data['chrom_descr_6'] = chrom_descr_6
        response_data['chrom_descr_6_unit'] = chrom_descr_6_unit
        response_data['chrom_descr_7'] = chrom_descr_7
        response_data['chrom_descr_7_unit'] = chrom_descr_7_unit
        response_data['chrom_descr_8'] = chrom_descr_8
        response_data['chrom_descr_8_unit'] = chrom_descr_8_unit
        response_data['chrom_descr_9'] = chrom_descr_9
        response_data['chrom_descr_9_unit'] = chrom_descr_9_unit
        response_data['new_descriptor'] = new_descriptor
        response_data['newdescriptor_unit'] = newdescriptor_unit
        response_data['uf_df_membrane_type'] = uf_df_membrane_type
        response_data['membrane_unit'] = membrane_unit
        response_data['uf_df_mht'] = uf_df_mht
        response_data['micro_holdtime_unit'] = micro_holdtime_unit
        response_data['uf_df_bht '] = uf_df_bht
        response_data['biochem_holdtime_unit'] = biochem_holdtime_unit
        response_data['inprocess_unit'] = inprocess_unit
        response_data['thaw_celltype'] = thaw_celltype
        response_data['celltype_unit'] = celltype_unit
        response_data['thaw_vessel_type'] = thaw_vessel_type
        response_data['vessel_unit'] = vessel_unit
        response_data['thaw_expansion_type'] = thaw_expansion_type
        response_data['expansion_unit'] = expansion_unit
        response_data['thaw_ipt'] = thaw_ipt
        response_data['inprocess_thaw_unit'] = inprocess_thaw_unit
        response_data['prodbio_media_type'] = prodbio_media_type
        response_data['media_type_unit'] = media_type_unit
        response_data['prodbio_vessel_volume'] = prodbio_vessel_volume
        response_data['vessel_volume_unit'] = vessel_volume_unit
        response_data['prodbio_composition'] = prodbio_composition
        response_data['composition_unit'] = composition_unit
        response_data['prodbio_ipt'] = prodbio_ipt
        response_data['prodbioinprocess_unit'] = prodbioinprocess_unit
        response_data['lowph_acid'] = lowph_acid
        response_data['lowph_base'] = lowph_base
        response_data['base_unit'] = base_unit
        response_data['lowph_mht'] = lowph_mht
        response_data['micro_holdtime_lowph_unit'] = micro_holdtime_lowph_unit
        response_data['lowph_bht'] = lowph_bht
        response_data['biochem_holdtime_lowph_unit'] = biochem_holdtime_lowph_unit
        response_data['inprocess_lowph_unit'] = inprocess_lowph_unit
        response_data['detergent_type'] = detergent_type
        response_data['detergent_unit'] = detergent_unit
        response_data['detergent_mht'] = detergent_mht
        response_data['micro_holdtime_det_unit '] = micro_holdtime_det_unit
        response_data['detergent_bht'] = detergent_bht
        response_data['biochem_holdtime_det_unit '] = biochem_holdtime_det_unit
        response_data['detergent_ipt'] = detergent_ipt
        response_data['inprocess_det_unit'] = inprocess_det_unit
        response_data['fil_filter'] = fil_filter
        response_data['filter_unit'] = filter_unit
        response_data['fil_filter_type'] = fil_filter_type
        response_data['fil_filter_unit'] = fil_filter_unit
        response_data['fil_ipt'] = fil_ipt
        response_data['inprocess_viral_unit '] = inprocess_viral_unit
        response_data['seedbio_comp '] = seedbio_comp
        response_data['seed_bio_composition_unit '] = seed_bio_composition_unit
        response_data['seedbio_mediatype '] = seedbio_mediatype
        response_data['seedbio_media_unit '] = seedbio_media_unit
        response_data['seedbio_ipt '] = seedbio_ipt
        response_data['seedbio_inprocess_unit '] = seedbio_inprocess_unit
        response_data['procname_text '] = procname_text
        response_data['procir_ircomments '] = procir_ircomments
        response_data['new_parameter '] = new_parameter
        response_data['ircomments_newproc '] = ircomments_newproc
        response_data['OBP'] = OBP
        response_data['obprisk_ircomments '] = obprisk_ircomments
        response_data['ircomments_apprisk  '] = ircomments_apprisk
        response_data['new_proc_comment '] = new_proc_comment
        response_data['Assign_Risk  '] = Assign_Risk
        response_data['applicant_risktext '] = applicant_risktext
        response_data['CPP_KPP '] = CPP_KPP
        response_data['cpp_ircomments '] = cpp_ircomments
        response_data['applicant_risk2 '] = applicant_risk2
        response_data['surr_applicant_risk_ranking '] = surr_applicant_risk_ranking
        response_data['ircomments_surrir '] = ircomments_surrir
        response_data['surprocessparameter '] = surprocessparameter
        response_data['surrproc_ircomments '] = surrproc_ircomments
        response_data['app_sur '] = app_sur
        response_data['ircomments_surrapp_risk '] = ircomments_surrapp_risk
        response_data['surriskselect '] = surriskselect
        response_data['risk_comment '] = risk_comment
        response_data['surrisk_text '] = surrisk_text
        response_data['surr_Assign_Risk '] = surr_Assign_Risk
        response_data['surrCPP_surrKPP '] = surrCPP_surrKPP
        response_data['ircomments_surrcpp '] = ircomments_surrcpp
        response_data['surrisk_text2 '] = surrisk_text2
        response_data['cppdropdownselect '] = cppdropdownselect
        response_data['characir_comments '] = characir_comments
        response_data['study_appropriate_select '] = study_appropriate_select
        response_data['appro_charac_ircomments '] = appro_charac_ircomments
        response_data['characterization_study_pk '] = characterization_study_pk
        response_data['pk_ircomments '] = pk_ircomments
        response_data['charac_range_low '] = charac_range_low
        response_data['charac_range_high '] = charac_range_high
        response_data['charac_range_ircomments= '] = charac_range_ircomments
        response_data['validation_select '] = validation_select
        response_data['prelir_ircomments '] = prelir_ircomments
        response_data['valid_range_low '] = valid_range_low
        response_data['valid_range_high '] = valid_range_high
        response_data['ircommentsvalrange '] = ircommentsvalrange
        response_data['par_ircomments '] = par_ircomments
        response_data['par_range_low '] = par_range_low
        response_data['par_range_high '] = par_range_high
        response_data['response_select'] = response_select
        response_data['pp_range_select'] = pp_range_select
        response_data['ircommentsprop_par'] = ircommentsprop_par
        response_data['acid_unit'] = acid_unit
        response_data['lowph_ipt'] = lowph_ipt
        response_data['applicant_risk_ranking'] = applicant_risk_ranking
        response_data['uf_df_ipt'] = uf_df_ipt

        ins = Riskeval(unitop_text=unitop_text, unitop_ircomments=unitop_ircomments,
                       harvest_descriptor=harvest_descriptor,
                       harvest_type_unit=harvest_type_unit,
                       chrom_descr_1=chrom_descr_1,
                       chrom_descr_1_unit=chrom_descr_1_unit,
                       chrom_descr_2=chrom_descr_2,
                       chrom_descr_2_unit=chrom_descr_2_unit,
                       chrom_descr_3=chrom_descr_3,
                       chrom_descr_3_unit=chrom_descr_3_unit,
                       chrom_descr_4=chrom_descr_4,
                       chrom_descr_4_unit=chrom_descr_4_unit,
                       chrom_descr_5=chrom_descr_5,
                       chrom_descr_5_unit=chrom_descr_5_unit,
                       chrom_descr_6=chrom_descr_6,
                       chrom_descr_6_unit=chrom_descr_6_unit,
                       chrom_descr_7=chrom_descr_7,
                       chrom_descr_7_unit=chrom_descr_7_unit,
                       chrom_descr_8=chrom_descr_8,
                       chrom_descr_8_unit=chrom_descr_8_unit,
                       chrom_descr_9=chrom_descr_9,
                       chrom_descr_9_unit=chrom_descr_9_unit,
                       new_descriptor=new_descriptor,
                       newdescriptor_unit=newdescriptor_unit,
                       uf_df_membrane_type=uf_df_membrane_type,
                       membrane_unit=membrane_unit,
                       uf_df_mht=uf_df_mht,
                       micro_holdtime_unit=micro_holdtime_unit,
                       uf_df_bht=uf_df_bht,
                       biochem_holdtime_unit=biochem_holdtime_unit,
                       inprocess_unit=inprocess_unit,
                       thaw_celltype=thaw_celltype,
                       celltype_unit=celltype_unit,
                       thaw_vessel_type=thaw_vessel_type,
                       vessel_unit=vessel_unit,
                       thaw_expansion_type=thaw_expansion_type,
                       expansion_unit=expansion_unit,
                       thaw_ipt=thaw_ipt,
                       inprocess_thaw_unit=inprocess_thaw_unit,
                       prodbio_media_type=prodbio_media_type,
                       media_type_unit=media_type_unit,
                       prodbio_vessel_volume=prodbio_vessel_volume,
                       vessel_volume_unit=vessel_volume_unit,
                       prodbio_composition=prodbio_composition,
                       composition_unit=composition_unit,
                       prodbio_ipt=prodbio_ipt,
                       prodbioinprocess_unit=prodbioinprocess_unit,
                       lowph_acid=lowph_acid,
                       lowph_base=lowph_base,
                       base_unit=base_unit,
                       lowph_mht=lowph_mht,
                       micro_holdtime_lowph_unit=micro_holdtime_lowph_unit,
                       lowph_bht=lowph_bht,
                       biochem_holdtime_lowph_unit=biochem_holdtime_lowph_unit,
                       inprocess_lowph_unit=inprocess_lowph_unit,
                       detergent_type=detergent_type,
                       detergent_unit=detergent_unit,
                       detergent_mht=detergent_mht,
                       micro_holdtime_det_unit=micro_holdtime_det_unit,
                       detergent_bht=detergent_bht,
                       biochem_holdtime_det_unit=biochem_holdtime_det_unit,
                       detergent_ipt=detergent_ipt,
                       inprocess_det_unit=inprocess_det_unit,
                       fil_filter=fil_filter,
                       filter_unit=filter_unit,
                       fil_filter_type=fil_filter_type,
                       fil_filter_unit=fil_filter_unit,
                       fil_ipt=fil_ipt,
                       inprocess_viral_unit=inprocess_viral_unit,
                       seedbio_comp=seedbio_comp,
                       seed_bio_composition_unit=seed_bio_composition_unit,
                       seedbio_mediatype=seedbio_mediatype,
                       seedbio_media_unit=seedbio_media_unit,
                       seedbio_ipt=seedbio_ipt,
                       seedbio_inprocess_unit=seedbio_inprocess_unit,
                       procname_text=procname_text,
                       procir_ircomments=procir_ircomments,
                       new_parameter=new_parameter,
                       ircomments_newproc=ircomments_newproc,
                       OBP=OBP,
                       obprisk_ircomments=obprisk_ircomments,
                       ircomments_apprisk=ircomments_apprisk,
                       new_proc_comment=new_proc_comment,
                       Assign_Risk=Assign_Risk,
                       applicant_risktext=applicant_risktext,
                       CPP_KPP=CPP_KPP,
                       cpp_ircomments=cpp_ircomments,
                       applicant_risk2=applicant_risk2,
                       surr_applicant_risk_ranking=surr_applicant_risk_ranking,
                       ircomments_surrir=ircomments_surrir,
                       surprocessparameter=surprocessparameter,
                       surrproc_ircomments=surrproc_ircomments,
                       app_sur=app_sur,
                       ircomments_surrapp_risk=ircomments_surrapp_risk,
                       surriskselect=surriskselect,
                       risk_comment=risk_comment,
                       surrisk_text=surrisk_text,
                       surr_Assign_Risk=surr_Assign_Risk,
                       surrCPP_surrKPP=surrCPP_surrKPP,
                       ircomments_surrcpp=ircomments_surrcpp,
                       surrisk_text2=surrisk_text2,
                       cppdropdownselect=cppdropdownselect,
                       characir_comments=characir_comments,
                       study_appropriate_select=study_appropriate_select,
                       appro_charac_ircomments=appro_charac_ircomments,
                       characterization_study_pk=characterization_study_pk,
                       pk_ircomments=pk_ircomments,
                       charac_range_low=charac_range_low,
                       charac_range_high=charac_range_high,
                       charac_range_ircomments=charac_range_ircomments,
                       validation_select=validation_select,
                       prelir_ircomments=prelir_ircomments,
                       valid_range_low=valid_range_low,
                       valid_range_high=valid_range_high,
                       ircommentsvalrange=ircommentsvalrange,
                       par_ircomments=par_ircomments,
                       par_range_low=par_range_low,
                       par_range_high=par_range_high,
                       response_select=response_select,
                       pp_range_select=pp_range_select,
                       ircommentsprop_par=ircommentsprop_par,
                       acid_unit=acid_unit,
                       lowph_ipt=lowph_ipt,
                       applicant_risk_ranking=applicant_risk_ranking,
                       uf_df_ipt=uf_df_ipt)

        ins.save()
        return JsonResponse(response_data)

    return render(request, "kasaapp/riskeval.html",
                  {"unitoperation": unit, "processparameter": pps, "surrogate": surrogate,
                   "riskeval_page": riskeval_page})


def summary(request):
    return render(request, "kasaapp/summary.html", {})


def overviewload(request):
    application_path = request.POST.get('application_path')
    applicant_name = request.POST.get('applicant_name')
    bla_number = request.POST.get('bla_number')
    review = request.POST.get('review')
    review_iteration = request.POST.get('review_iteration')
    review_decision = request.POST.get('review_decision')
    designation = request.POST.get('designation')
    prop_name = request.POST.get('prop_name')
    non_prop_name = request.POST.get('non_prop_name')
    obp_name = request.POST.get('obp_name')
    dosage_form = request.POST.get('dosage_form')
    strength_potency = request.POST.get('strength_potency')
    route_administration = request.POST.get('route_administration')
    primary_assessor = request.POST.get('primary_assessor')
    secondary_assessor = request.POST.get('secondary_assessor')

    return render(request, "kasaapp/overview.html", {"bla_number": bla_number,
                                                     "applicant_name": applicant_name,
                                                     "application_path": application_path,
                                                     "review": review,
                                                     "review_iteration": review_iteration,
                                                     "review_decision": review_decision,
                                                     "designation": designation,
                                                     "prop_name": prop_name,
                                                     "non_prop_name": non_prop_name,
                                                     "obp_name": obp_name,
                                                     "dosage_form": dosage_form,
                                                     "strength_potency": strength_potency,
                                                     "route_administration": route_administration,
                                                     "primary_assessor": primary_assessor,
                                                     "secondary_assessor": secondary_assessor,
                                                     })
