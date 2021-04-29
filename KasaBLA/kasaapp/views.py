from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render
from .models import unitoperation
from .models import processparameter
from .models import Overview
from django.core.mail import send_mail
from django.core import serializers
from django.http import JsonResponse
import json


def home(request):
    return render(request, "kasaapp/home.html", {})


def characterization(request):
    processparam = processparameter.objects.all()
    unitops = unitoperation.objects.all()
    return render(request, "kasaapp/characterization.html",
                  {"unit": unitops, "pp": processparam})


def overview(request):
    overview_page = Overview.objects.all()
    response_data = {}

    if request.POST.get('action') == 'post':
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
    unit = unitoperation.objects.all()
    pps = processparameter.objects.all()
    surrogate = processparameter.objects.exclude(processparameter_name="New process parameter")
    return render(request, "kasaapp/riskeval.html",
                  {"unitoperation": unit, "processparameter": pps, "surrogate": surrogate})


def summary(request):
    if request.is_ajax and request.method == 'GET':
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
                                                        "surpreliminaryrisk2": surrisk2})
    if request.is_ajax and request.method == 'POST':
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
                                                        "surpreliminaryrisk2": surrisk2})
