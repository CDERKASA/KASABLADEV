
function unit(u) {
        var x = document.getElementById(u).textContent;
        alert(x);
        document.getElementById(u).innerHTML = x;
        var b = document.getElementById("unitoperations");
        var option = document.createElement("option");
        for (var i=0; i<b.length; i++){
            var opt = b.options[i];
            if (opt.text === x){
                return;
            }
        }
        option.text = x;
        b.append(option);
       if(option.text === "Chromatography-Protein A") {
        option.value = 1;
       } else if(option.text === "Chromatography-Mixed Mode") {
        option.value = 2;
       }  else if(option.text === "Chromatography-Hydrophobic Interaction") {
        option.value = 3;
       }  else if(option.text === "Chromatography-Anion Exchange") {
        option.value = 4;
       }   else if(option.text === "Chromatography-Cation Exchange") {
        option.value = 5;
       }    else if(option.text === "Cell Culture - Seed Bioreactor") {
        option.value = 6;
       }    else if(option.text === "Cell Culture - Vial thaw and inoculation expansion") {
        option.value = 7;
       }    else if(option.text === "Cell Culture - Production Bioreactor") {
        option.value = 8;
       }    else if(option.text === "Cell Culture - Harvest") {
        option.value = 9;
       }    else if(option.text === "Ultrafiltration/Diafiltration") {
        option.value = 10;
       }    else if(option.text === "Viral Filtration") {
         option.value = 11;
       }   else if(option.text === "Virus inactivation - Low pH") {
        option.value = 12;
       }    else {
        option.value = 13;
       }
       $("#draggable").append($('<li></li>').text(x));
       $("#draggable").sortable();
};

$(document).ready(function(){
    var $select1 = $('#unitoperations'),
        $select2 = $('#processparameter'),
        $OBPrisk = $('#riskselect');

    $options2 = $select2.find('option');
    $span3 = $OBPrisk.find('span');


    $select1.on('change', function() {
         $span3.each(function() {
         this.style.display = "none";
    });

  $select2.html($options2.filter(
     function() {
       var opt_val = this.value;
         if (opt_val === "default") {
            return true;
         }
         return opt_val.includes('-' + $select1.val() + '-');
     }));
     $select2.val("default");
     }).trigger('change');

  $select2.on('change', function() {
    var selected = this.value;
    $span3.each(function() {
       if ($(this).attr('id') === selected) {
          this.style.display = "inline";
       } else {
           this.style.display = "none";
       }
});
}).trigger('change');

var $select11 = $('#unitoperations'),
    $select22 = $('#surprocselect'),
    $surrogateOBPrisk = $('#surriskselect');

    $options22 = $select22.find('option');
    $span33 = $surrogateOBPrisk.find('span1');


    $select11.on('change', function() {
    $span33.each(function() {
       this.style.display = "none";
  });

    $select22.html($options22.filter(
       function() {
          var opt_val = this.value;
          if (opt_val === 'default') {
              return true;
          }
       return opt_val.includes('-' + $select11.val() + '-');
  }));
  $select22.val("default");
}).trigger('change');

   $select22.on('change', function() {
       var selected = this.value;
       $span33.each(function() {
          if ($(this).attr('id') === selected) {
              this.style.display = "inline";
          } else {
              this.style.display = "none";
          }
  });
}).trigger('change');

});




function descriptorsnone() {
        var chromatography_descriptor1 = document.getElementById("chromatography_descriptor_block");
        var cellculture_descriptor1 = document.getElementById("cellculture_descriptor_block");
        var uf_df_descriptor1 = document.getElementById("uf_df_descriptor_block");
        var thaw_descriptor1 = document.getElementById("thaw_descriptor_block");
        var prodbio_descriptor1 = document.getElementById("prodbio_descriptor_block");
        var lowph_descriptor1 = document.getElementById("lowph_descriptor_block");
        var detergent_descriptor1 = document.getElementById("detergent_block");
        var viral_fil_descriptor1 = document.getElementById("viral_fil_block");
        var seedbio_descriptor1 = document.getElementById("seedbio_block");

        chromatography_descriptor1.style.display = "none";
        cellculture_descriptor1.style.display = "none";
        uf_df_descriptor1.style.display = "none";
        thaw_descriptor1.style.display = "none";
        prodbio_descriptor1.style.display = "none";
        lowph_descriptor1.style.display = "none";
        detergent_descriptor1.style.display = "none";
        viral_fil_descriptor1.style.display = "none";
        seedbio_descriptor1.style.display = "none";
    }
function unitFun() {
        var unitoperations = document.getElementById("unitoperations");
        var unitop_drop = unitoperations.options[unitoperations.selectedIndex].text;
        var unit_name = document.getElementById("unit_name");
        unit_name.innerHTML=unitop_drop;

        var chromatography_descriptor = document.getElementById("chromatography_descriptor_block");
        var cellculture_descriptor = document.getElementById("cellculture_descriptor_block");
        var uf_df_descriptor = document.getElementById("uf_df_descriptor_block");
        var thaw_descriptor = document.getElementById("thaw_descriptor_block");
        var prodbio_descriptor = document.getElementById("prodbio_descriptor_block");
        var lowph_descriptor = document.getElementById("lowph_descriptor_block");
        var detergent_descriptor = document.getElementById("detergent_block");
        var viral_fil_descriptor = document.getElementById("viral_fil_block");
        var seedbio_descriptor = document.getElementById("seedbio_block");

        if (unitop_drop === "Cell Culture - Seed Bioreactor") {
            descriptorsnone();
            seedbio_descriptor.style.display = "block";
        } else if (unitop_drop === "Cell Culture - Vial thaw and inoculation expansion") {
            descriptorsnone();
            thaw_descriptor.style.display = "block";
        } else if (unitop_drop === "Cell Culture - Production Bioreactor") {
            descriptorsnone();
            prodbio_descriptor.style.display = "block";
        } else if (unitop_drop === "Cell Culture - Harvest") {
            descriptorsnone();
            cellculture_descriptor.style.display = "block";
        } else if (unitop_drop === "Ultrafiltration/Diafiltration") {
            descriptorsnone();
            uf_df_descriptor.style.display = "block";
        } else if (unitop_drop === "Viral Filtration") {
            descriptorsnone();
            viral_fil_descriptor.style.display = "block";
        } else if (unitop_drop === "Virus inactivation - Low pH") {
            descriptorsnone();
            lowph_descriptor.style.display = "block";
        } else if (unitop_drop === "--Select Unit Operation--") {
            descriptorsnone();
        } else {
            descriptorsnone();
            chromatography_descriptor.style.display = "block";
        }
    }
function blockmyFunction1() {
        var new_pp1 = document.getElementById("new_pp");
        var surrogate_yesno1 = document.getElementById("surrogate_yesno");
        var surrogate_pp1 = document.getElementById("surrogate_pp");
        var applicant_risk_sur1 = document.getElementById("applicant_risk_sur");
        var sur_risk1 = document.getElementById("sur_risk");
        var surrogate_agree_mssg1 = document.getElementById("surrogate_agree_mssg");
        var surrogate_final_risk_block1 = document.getElementById("surrogate_final_risk_block");
        var surrogate_notagree_m1 = document.getElementById("surrogate_notagree_m");
        var surrogate_notagree1 = document.getElementById("surrogate_notagree");
        var surrogate_cpp1 = document.getElementById("surrogate_cpp");
        var surrogate_ntagree_final_risk_block1 = document.getElementById("surrogate_ntagree_final_risk_block");

        new_pp1.style.display = "none";
        surrogate_yesno1.style.display = "none";
        surrogate_pp1.style.display = "none";
        applicant_risk_sur1.style.display = "none";
        sur_risk1.style.display = "none";
        surrogate_agree_mssg1.style.display = "none";
        surrogate_final_risk_block1.style.display = "none";
        surrogate_notagree_m1.style.display = "none";
        surrogate_notagree1.style.display = "none";
        surrogate_cpp1.style.display = "none";
        surrogate_ntagree_final_risk_block1.style.display = "none";
    }
function myFunction() {
        var ranking = document.getElementById("Ranking");
        var selectrisk = document.getElementById("riskselect");
        var applicantrisk = document.getElementById("risk");
        var finalrisk = document.getElementById("final_risk_block");

        var agree_message = document.getElementById("agree_message");
        var ntagree = document.getElementById("notagree");
        var ntagree_message = document.getElementById("notagree_message");
        var finalrisk_m = document.getElementById("Final_Risk_Ranking_ntagree");
        var assignrisk_m = document.getElementById("Assign_Risk");
        var cpp = document.getElementById("cpp");
        var cpp_kpp = document.getElementById("CPP_KPP");
        cpp_kpp.selectedIndex = "default";
        assignrisk_m.selectedIndex = "default";
        var finalrisk_ntagree = document.getElementById("ntagree_final_risk_block");
        var risk_r = selectrisk.innerText;
        var risk_p = applicantrisk.options[applicantrisk.selectedIndex].text;
        var risk_n = assignrisk_m.options[assignrisk_m.selectedIndex].text;
        finalrisk_m.innerHTML = "";
        blockmyFunction1();


            if (risk_p === risk_r) {
                    blockmyFunction1();
                    ranking.innerHTML = risk_r;
                    document.getElementById("applicant_risktext").value = ranking.innerHTML;
                    finalrisk.style.display = "block";
                    agree_message.style.display = "block";
                    ntagree.style.display = "none";
                    ntagree_message.style.display = "none";
                    finalrisk_ntagree.style.display = "none";
                    cpp.style.display= "block";
                    cpp_kpp.selectedIndex = "default";
                    if (risk_p === "Low risk") {
                    blockmyFunction1();
                    cpp.style.display = "none";
                    } else {
                    blockmyFunction1();
                    cpp.style.display = "block";
                    cpp_kpp.selectedIndex = "default";
                    }
            } else {
                if (risk_p === "--Select--") {
                    agree_message.style.display = "none";
                    finalrisk.style.display = "none";
                    ntagree_message.style.display = "none";
                    ntagree.style.display = "none";
                    finalrisk_ntagree.style.display = "none";
                    cpp.style.display= "none";
                } else {
                    blockmyFunction1();
                    agree_message.style.display = "none";
                    finalrisk.style.display = "none";
                    ntagree_message.style.display = "block";
                    ntagree.style.display = "block";
                    finalrisk_ntagree.style.display = "block";
                }
            }
        }
function myFun() {
    var assignrisk_m1 = document.getElementById("Assign_Risk");
    var risk_n1 = assignrisk_m1.options[assignrisk_m1.selectedIndex].text;
    var finalrisk_m1 = document.getElementById("Final_Risk_Ranking_ntagree");
    var cpp1 = document.getElementById("cpp");
    var cpp_kpp1 = document.getElementById("CPP_KPP");
    cpp_kpp1.selectedIndex = "default";

    if (risk_n1 === "--Select--") {
        blockmyFunction1();
        finalrisk_m1.style.visibility = "hidden";
        cpp1.style.display = "none";
        } else if (risk_n1 === "Low risk") {
        blockmyFunction1();
        cpp1.style.display = "none";
        finalrisk_m1.style.visibility = "visible";
        finalrisk_m1.innerHTML = risk_n1;
        document.getElementById("applicant_risk2").value = risk_n1;
        } else {
        blockmyFunction1();
        cpp1.style.display = "block";
        cpp_kpp1.selectedIndex = "default";
        finalrisk_m1.style.visibility = "visible";
        finalrisk_m1.innerHTML = risk_n1;
        document.getElementById("applicant_risk2").value = risk_n1;
    }
}

function blockmyFunction() {
        var agree_message1 = document.getElementById("agree_message");
        var finalrisk1 = document.getElementById("final_risk_block");
        var notagree_m1 = document.getElementById("notagree_message");
        var notagree1 = document.getElementById("notagree");
        var cpp1 = document.getElementById("cpp");
        var ntagree_final_risk_block1 = document.getElementById("ntagree_final_risk_block");

        agree_message1.style.display = "none";
        finalrisk1.style.display = "none";
        notagree_m1.style.display = "none";
        notagree1.style.display = "none";
        cpp1.style.display = "none";
        ntagree_final_risk_block1.style.display = "none";
    }

function newppFun() {
     var procdrop11 = document.getElementById("processparameter");
     var proc_para11 = procdrop11.options[procdrop11.selectedIndex].text;
     var newpp_block11 = document.getElementById("new_pp");
     var sur_risk11 = document.getElementById("sur_risk");
     var surrogate_yesno11 = document.getElementById("surrogate_yesno");
     var surr_yesno11 = document.getElementById("surr_yesno");
     var applicant_risk11 = document.getElementById("applicant_risk");
     var obp_risk11 = document.getElementById("obp_risk");
     var risk1 = document.getElementById("risk");
     risk1.selectedIndex = "default";
     var newppinput =  document.getElementById("new_parameter");
     newppinput.value = "";
     blockmyFunction();
     if (proc_para11 === "New process parameter") {
        blockmyFunction();
        newpp_block11.style.display = "block";
        sur_risk11.style.display="block";
        surrogate_yesno11.style.display ="block";
        applicant_risk11.style.display ="none";
        obp_risk11.style.display ="none";
     } else {
        blockmyFunction();
        document.getElementById("procname_text").value = proc_para11;

        surr_yesno11.selectedIndex = "default";
        applicant_risk11.style.display = "block";
        obp_risk11.style.display = "block";
        myFunction();

     }
}

function yesnoFun() {
    blockmyFunction();

    var applicant_risk1 = document.getElementById("applicant_risk");
    var obp_risk1 = document.getElementById("obp_risk");

    var applicant_risk_sur = document.getElementById("applicant_risk_sur");
    var surrogate_pp =  document.getElementById("surrogate_pp");
    var finalrisk_sur = document.getElementById("surrogate_final_risk_block");
    var agree_message_sur = document.getElementById("surrogate_agree_mssg");
    var finalrisk_m_sur = document.getElementById("surr_Final_Risk_Ranking_ntagree");
    var ntagree_sur = document.getElementById("surrogate_notagree");
    var ntagree_m_sur = document.getElementById("surrogate_notagree_m");
    var cpp_surr = document.getElementById("surrogate_cpp");
    var finalrisk_ntagree_sur = document.getElementById("surrogate_ntagree_final_risk_block");
    var sur_risk = document.getElementById("sur_risk");
    var app_sur = document.getElementById("app_sur");
    app_sur.selectedIndex = "default";
    var newppinput =  document.getElementById("new_parameter");
    newppinput.value = "";
    var surprocselect =  document.getElementById("surprocselect");
    surprocselect.selectedIndex = "default";
    var sur_riskselect = document.getElementById("surriskselect");
    var sur_riskselectdrop = "";
    var assignrisk_m_sur = document.getElementById("surr_Assign_Risk");
    assignrisk_m_sur.selectedIndex = "default";
    finalrisk_m_sur.innerHTML = "";
    var cpp_kpp_sur1 = document.getElementById("surr_CPP_KPP");
    cpp_kpp_sur1.selectedIndex = "default";
    var surrogate_yesno= document.getElementById("surrogate_yesno");
    var surr_yesno= document.getElementById("surr_yesno");
    var sur_yesno_drop = surr_yesno.options[surr_yesno.selectedIndex].text;

    if (sur_yesno_drop === "--Select--") {
        blockmyFunction();
        applicant_risk1.style.display ="none";
        obp_risk1.style.display ="none";
        applicant_risk_sur.style.display="none";
        surrogate_pp.style.display ="none";
        finalrisk_sur.style.display = "none";
        agree_message_sur.style.display = "none";
        ntagree_sur.style.display = "none";
        ntagree_m_sur.style.display = "none";
        cpp_surr.style.display = "none";
        finalrisk_ntagree_sur.style.display = "none";
        sur_risk.style.display="none";
    } else if (sur_yesno_drop === "YES") {
        blockmyFunction();
        applicant_risk1.style.display ="none";
        obp_risk1.style.display ="none";
        applicant_risk_sur.style.display="block";
        surrogate_pp.style.display ="block";


        finalrisk_sur.style.display = "none";
        agree_message_sur.style.display = "none";
        ntagree_sur.style.display = "none";
        ntagree_m_sur.style.display = "none";
        cpp_surr.style.display = "none";
        finalrisk_ntagree_sur.style.display = "none";
        sur_risk.style.display="block";
    } else {
        blockmyFunction();
        applicant_risk1.style.display ="none";
        obp_risk1.style.display ="none";
        applicant_risk_sur.style.display="block";
        surrogate_pp.style.display ="none";
        sur_risk.style.display="none";
        finalrisk_sur.style.display = "none";
        ntagree_sur.style.display = "block";
        agree_message_sur.style.display = "none";
        ntagree_m_sur.style.display = "none";
        cpp_surr.style.display = "block";
        finalrisk_ntagree_sur.style.display = "block";
    }
}

function surrppFun() {
    var app_sur = document.getElementById("app_sur");
    app_sur.selectedIndex = "default";
    var ntagree_m_sur = document.getElementById("surrogate_notagree_m");
    ntagree_m_sur.style.display = "none";
    var ntagree_sur = document.getElementById("surrogate_notagree");
    ntagree_sur.style.display = "none";
    var agree_message_sur = document.getElementById("surrogate_agree_mssg");
    agree_message_sur.style.display = "none";
    var finalrisk_sur = document.getElementById("surrogate_final_risk_block");
    finalrisk_sur.style.display = "none";
    var cpp_surr = document.getElementById("surrogate_cpp");
    cpp_surr.style.display = "none";
    var finalrisk_ntagree_sur = document.getElementById("surrogate_ntagree_final_risk_block");
    finalrisk_ntagree_sur.style.display = "none";
    var surprocselect = document.getElementById("surprocselect");
     var surprocselectdrop = surprocselect.options[surprocselect.selectedIndex].text;
      document.getElementById("surprocessparameter").value = surprocselectdrop;


}
function myFunction1() {
        var surrogate_pp =  document.getElementById("surrogate_pp");
        var sur_risk = document.getElementById("sur_risk");
        var surrogate_yesno= document.getElementById("surrogate_yesno");
        var surr_yesno= document.getElementById("surr_yesno");



        var applicant_risk_sur = document.getElementById("applicant_risk_sur");
        var app_sur = document.getElementById("app_sur");
        var sur_riskselect = document.getElementById("surriskselect");
        var sur_assessor = document.getElementById("surr_Assessor");
        var sur_ranking = document.getElementById("surr_Ranking");

        var agree_message_sur = document.getElementById("surrogate_agree_mssg");
        var finalrisk_sur = document.getElementById("surrogate_final_risk_block");
        var ntagree_sur = document.getElementById("surrogate_notagree");
        var ntagree_m_sur = document.getElementById("surrogate_notagree_m");
        var ntagree_message_sur = document.getElementById("surr_notagree_message");
        var finalrisk_m_sur = document.getElementById("surr_Final_Risk_Ranking_ntagree");
        finalrisk_m_sur.innerHTML = "";
        var assignrisk_m_sur= document.getElementById("surr_Assign_Risk");
        var cpp_surr = document.getElementById("surrogate_cpp");
        var finalrisk_ntagree_sur = document.getElementById("surrogate_ntagree_final_risk_block");

        var applicant_risk1 = document.getElementById("applicant_risk");
        var obp_risk1 = document.getElementById("obp_risk");
        var risk1 = document.getElementById("risk");
        risk1.selectedIndex = "default";
        assignrisk_m_sur.selectedIndex = "default";

        var newppinput =  document.getElementById("new_parameter");
        newppinput.value = "";
        var cpp_kpp_sur1 = document.getElementById("surr_CPP_KPP");
        cpp_kpp_sur1.selectedIndex = "default";

        var surr_yesno= document.getElementById("surr_yesno");
        var sur_yesno_drop = surr_yesno.options[surr_yesno.selectedIndex].text;

        blockmyFunction();

        var app_sur_drop = app_sur.options[app_sur.selectedIndex].text;
        var sur_riskselectdrop = sur_riskselect.innerText;

        if (sur_yesno_drop === "YES") {
            if (app_sur_drop === sur_riskselectdrop) {
            blockmyFunction();
            applicant_risk1.style.display ="none";
            obp_risk1.style.display ="none";
            finalrisk_sur.style.display = "block";
            sur_ranking.innerHTML = sur_riskselectdrop;
            document.getElementById("surrisk_text").value= sur_ranking.innerHTML ;

            sur_assessor.innerHTML="Assessor Agrees with Applicant Risk Ranking";
            agree_message_sur.style.display = "block";
            finalrisk_m_sur.style.display = "block";
            ntagree_sur.style.display = "none";
            ntagree_m_sur.style.display = "none";
            cpp_surr.style.display = "none";
            finalrisk_ntagree_sur.style.display = "none";
                if (app_sur_drop === "Low risk") {
                blockmyFunction();
                applicant_risk1.style.display ="none";
                obp_risk1.style.display ="none";
                cpp_surr.style.display = "none";
                finalrisk_m_sur.style.visibility = "visible";
                finalrisk_m_sur.innerHTML = app_sur_drop
                } else if (app_sur_drop === "Medium risk" || "High risk") {
                blockmyFunction();
                applicant_risk1.style.display ="none";
                obp_risk1.style.display ="none";
                cpp_surr.style.display = "block";
                finalrisk_m_sur.style.visibility = "visible";
                finalrisk_m_sur.innerHTML = app_sur_drop;
                } else {
                blockmyFunction();
                applicant_risk1.style.display ="none";
                obp_risk1.style.display ="none";
                cpp_surr.style.display = "none";
                finalrisk_m_sur.style.visibility = "hidden";
                }
            } else {
            blockmyFunction();
            applicant_risk1.style.display ="none";
            obp_risk1.style.display ="none";
            agree_message_sur.style.display = "none";
            finalrisk_sur.style.display = "none";
            finalrisk_m_sur.style.display = "block";
            ntagree_sur.style.display = "block";
            ntagree_m_sur.style.display = "block";
            ntagree_message_sur.innerHTML = "Assessor does not agree with Applicant risk ranking";
            cpp_surr.style.display = "block";
            finalrisk_ntagree_sur.style.display = "block";
            sur_ranking.innerHTML = sur_riskselectdrop;
            }
        } else {
            myFun1();
        }
}

function myFun1() {
    var assignrisk_m_sur1 = document.getElementById("surr_Assign_Risk");
    var risk_n_sur1 = assignrisk_m_sur1.options[assignrisk_m_sur1.selectedIndex].text;
    var finalrisk_m_sur1 = document.getElementById("surr_Final_Risk_Ranking_ntagree");
    var cpp_sur1 = document.getElementById("surrogate_cpp");
    var cpp_kpp_sur1 = document.getElementById("surr_CPP_KPP");
    cpp_kpp_sur1.selectedIndex = "default";
    finalrisk_m_sur1.innerHTML = "";

    if (risk_n_sur1 === "--Select--") {
        blockmyFunction();
        finalrisk_m_sur1.style.visibility = "hidden";
        cpp_sur1.style.display = "none";
    } else if (risk_n_sur1 === "Low risk") {
        blockmyFunction();
        cpp_sur1.style.display = "none";
        finalrisk_m_sur1.style.visibility = "visible";
        finalrisk_m_sur1.innerHTML = risk_n_sur1;
         document.getElementById("surrisk_text2").value = risk_n_sur1;
    } else {
        blockmyFunction();
        cpp_sur1.style.display = "block";
        cpp_kpp_sur1.selectedIndex = "default";
        finalrisk_m_sur1.style.visibility = "visible";
        finalrisk_m_sur1.innerHTML = risk_n_sur1;
          document.getElementById("surrisk_text2").value = risk_n_sur1;
    }
}

function summary () {
    $('.ajaxProgress').show();
    console.log("create summary is working")
    $.ajax({
        url : "summary",
        dataType: "json",
        async: true,
        type : "POST",
        data : { csrfmiddlewaretoken: '{(csrf_token)}}',
                Unit name: $('#unitoptext').val(),

        },

        // handle a successful response
        success : function(json) {
            $('summary').html(json.message);
            $('.ajaxProgress').hide();
            console.log(json);
            console.log("success");
        }


    });
}

$('#overviewForm').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")
    $.ajax({
        url: "overview",
        type: "POST",
        async: "true",
        data: { csrfmiddlewaretoken: '{{ csrf_token }}',
                application_path: 'application_path',
                review: 'review',
                bla_number: 'bla_number',
                applicant_name: 'applicant_name',
                prop_name: 'prop_name',
                non_prop_name: 'non_prop_name',
                obp_name: 'obp_name',
                dosage_form: 'dosage_form',
                strength_potency: 'strength_potency',
                route_administration: 'route_administration',
                primary_assessor: 'primary_assessor',
                secondary_assessor: 'secondary_assessor',
                orphan_drug: 'orphan_drug',
                breakthrough: 'breakthrough',
                designation: 'designation',
                reviewer_decision: 'reviewer_decision',
                submission_date: 'submission_date'
                review_iteration: 'review_iteration'

        }
    })
    });