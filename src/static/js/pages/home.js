

const eFormProductSearch = {
    form: '#product-search-form',

    inputs: {
        location: '#product-search-form-input-location',
        dates: '#product-search-form-input-dates',
        category: '#product-search-form-input-category',
    },

    dropdownDataAttr:'data-product-category-sub-id',

    classes: {
        input: '.product-search-form-input',
    },

    dateRangesFlatpick: null,

    getInputValues: function() {
        let values = {};
        
        values.location_id = $(eFormProductSearch.inputs.location).val();

        const dates = eFormProductSearch.getFlatPickrRangeDates();
        values.starts_on = dates.startsOn;
        values.ends_on = dates.endsOn;
        
        
        values.product_categories_sub_id = eFormProductSearch.getProductCategorySubId();

        return values;
    },


    getProductCategorySubId: function() {
        const result = $(eFormProductSearch.inputs.category).attr(eFormProductSearch.dropdownDataAttr);
        return result;
    },

    /************************************************
    Returns the starts on and ends on values in a flatpickr date range.
    *************************************************/
    getFlatPickrRangeDates: function() {
        if (eFormProductSearch.dateRangesFlatpick.selectedDates.length == 0) {
            return null;
        }

        let out1 = DateTime.fromJSDate(eFormProductSearch.dateRangesFlatpick.selectedDates[0]); // starts on
        let out2 = DateTime.fromJSDate(eFormProductSearch.dateRangesFlatpick.selectedDates[1]); // ends on

        const result = {
            startsOn: out1.toISODate(),
            endsOn: out2.toISODate(),
        }

        return result;
    }

}






/**********************************************************
Main logic
**********************************************************/
$(document).ready(function() {
    loadPlugins();

    loadCategories();
});


/**********************************************************
Loads all of the js plugins
**********************************************************/
function loadPlugins() {
    loadSelect2();
    initFlatpickrs();
}


/**********************************************************
Loads the select2 library on the location input
**********************************************************/
function loadSelect2() {
    $(eFormProductSearch.inputs.location).select2({
        minimumInputLength: 3,
        theme: 'bootstrap4',
        ajax: {
            delay: 150,
            url: ApiWrapper.URLS.SEARCH.LOCATIONS,
            placeholder: "Select a state",
            allowClear: true,
            data: function (params) {
                const urlParms = {      // set the request url ?parms
                    q: params.term,
                }                
                return urlParms;
            },
            processResults: function (data) {
                const processedResults = processLocationSearchApiResponse(data);
                return processedResults;
            }
        },
        
    });
}

/**********************************************************
Process the api response data for the location search request.
It is transformed into the recognized format for select2.
**********************************************************/
function processLocationSearchApiResponse(apiResponse) {
    let processedData = [];
    for (let count = 0; count < apiResponse.length; count++) {
        const location = apiResponse[count];
        const text = `${location.city}, ${location.state_name}`;
        processedData.push({id: location.id, text: text});
    }
    
    return ({results: processedData});
}


/**********************************************************
Initialize the flat pickr inputs
**********************************************************/
function initFlatpickrs() {
    eFormProductSearch.dateRangesFlatpick = $(eFormProductSearch.inputs.dates).flatpickr({
        altInput: true,
        altFormat: "F j, Y",
        dateFormat: "Y-m-d",
        mode: "range",
        minDate: "today",
    });
}


/**********************************************************
Returns the product search date range input values.

Return value is an object containing the fields:
    - startsOn
    - endsOn
**********************************************************/
function getFlatPickrRangeDates() {   
    if (eFormProductSearch.dateRangesFlatpick.selectedDates.length == 0) {
        return null;
    }

    let out1 = DateTime.fromJSDate(eFormProductSearch.dateRangesFlatpick.selectedDates[0]); // starts on
    let out2 = DateTime.fromJSDate(eFormProductSearch.dateRangesFlatpick.selectedDates[1]); // ends on

    const result = {
        startsOn: out1.toISODate(),
        endsOn: out2.toISODate(),
    }

    return result;
}


/**********************************************************
Fetch the product category data from the API.
**********************************************************/
function loadCategories() {
    ApiWrapper.requestGetProductCategories(loadCategoriesSuccess, loadCategoriesError);
}

/**********************************************************
Callback for an unsuccessful fetch of the product categories (loadCategories)
**********************************************************/
function loadCategoriesError(xhr, status, error) {
    console.error('Error: loadCategoriesError')
    console.error(xhr);
    console.error(status);
    console.error(error);
}

/**********************************************************
Callback for a successful fetch of the product categories (loadCategories)
**********************************************************/
function loadCategoriesSuccess(result,status,xhr) {
    const categories = sortCategories(result);
    let minors = genertateMinorCategoryMap(categories);
    let html = generateCategorieshDropdownHtml(minors);

    $(eFormProductSearch.inputs.category).find('.dropdown-menu').html(html);
}

/**********************************************************
Sorts the list of product categories by Minor, Sub category.
**********************************************************/
function sortCategories(unsortedCategories) {
    // sort by sub category first
    const sortedCategories = unsortedCategories.sort(function(a, b) {
        const subA = a.sub_name.toUpperCase();
        const subB = b.sub_name.toUpperCase();

        return (subA < subB) ? -1 : 1;
    });

    // then sort by minor
    sortedCategories.sort(function(a, b) {
        const minorA = a.minor_name.toUpperCase();
        const minorB = b.minor_name.toUpperCase();

        return (minorA < minorB) ? -1 : 1;
    });

    return sortedCategories;
}

/**********************************************************
Transforms a list of product category objects into a map:
    key = minor category id
    value = object(name, subs: [])
**********************************************************/
function genertateMinorCategoryMap(categoriesTableList) {
    let minors = {};

    // break down the categories into a map of minor categories with an empty list for the sub categories
    for (const cat of categoriesTableList) {
        minors[cat.minor_id] = {
            name: cat.minor_name,
            subs: [],
        }
    }

    // insert all the sub categories into the sub category list
    for (const cat of categoriesTableList) {
        const sub = {
            id: cat.sub_id,
            name: cat.sub_name,
        }
        minors[cat.minor_id].subs.push(sub);
    }

    return minors;
}

/**********************************************************
Generates the dropdown menu html for the #product-search-form-input-category.
The input is a "minor product category" map generated by genertateMinorCategoryMap.
**********************************************************/
function generateCategorieshDropdownHtml(minorCategoriesMap) {
    let html = '';

    for (const minorID of Object.keys(minorCategoriesMap)) {
        const minorName = minorCategoriesMap[minorID].name;

        html += `<h6 class="dropdown-header">${minorName}</h6>`;
        
        // generate the html of the sub categories
        for (const sub of minorCategoriesMap[minorID].subs) {
            html += getSubCategoryDropdownHtml(sub.id, sub.name);
        }

        html += `<div class="dropdown-divider"></div>`;
    }

    return html;
}

/**********************************************************
Generates the dropdown menu item html for a single sub category.
**********************************************************/
function getSubCategoryDropdownHtml(id, name) {
    let html = `<button class="dropdown-item" type="button" data-category-sub-id="${id}">${name}</button>`;
    return html;
}

function getTheValues() {

    let result = eFormProductSearch.getInputValues();
    console.log(result);
}











