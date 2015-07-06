$(document).ready(function(){
	//fdahead-nav
	$('.fdahead-nav-toggle').click(function () {
		$('.fdahead-nav').toggleClass('active', 300);
		if ($('.fdahead-nav').is(':hidden')) {
			$('.fdahead-nav-toggle').html('<span>show navigation</span>');
			
		} else {
			$('.fdahead-nav-toggle').html('<span>hide navigation</span>');
		}
		$('.nav').removeClass('active');
		$('.nav-toggle').html('show nav box');
	});
	
	$( ".fda-tabs-interface" ).tabs();
	$( ".fda-accordion-interface" ).accordion({
		collapsible: true,
        active: false,
		heightStyle: "content",
        animate: 100,
        activate: accordionActivate
	});
  
    // search bar functionality
    var searchOptions = ['search_labels', 'search_events', 'search_enforcements'];

    // search go button onclick handler
    $("#search-category").click(function() {
        var url_category = $('#select-category').val();
        var search_term = $('#search-term').val();
        var search_state = $('#search-state').val();

        // if user types something or uses autocomplete, look for it in states
        if (search_state) {
            $(usStates).each(function() {
                if (search_state == this.value || search_state == this.label) {
                    search_state = this.value;
                    $('#search-state').val(search_state);
                }
            });
        }

        // stop the click event if the search term or category is falsey.
        var search_input = search_term || search_state;

        if(!search_input || !url_category) {
            return false;
        }

        if (url_category === 'search_labels') {
            $('form').attr("action", urlLabels).submit();
        }
        else if (url_category === 'search_events') {
            $('form').attr("action", urlEvents).submit();
        }
        else if (url_category === 'search_enforcements') {
            $('form').attr("action", urlEnforcements).submit();
        }
        else if (url_category === 'search_manufacturers') {
            $('form').attr("action", urlManufacturers).submit();
        }
        else {
            console.log('unknown category' + url_category);
            return false;
        }
    });

    // search bar typeahead using jquery-ui and states list in json
    $("#search-state").autocomplete({
        source: usStates,
        delay: 200,
        minLength: 1
    });

    // function to switch the text input from general to state with typeahead
    function changeInput() {
        if ($('#select-category').val() === 'search_enforcements') {
           $('#search-term').hide().prop('name', '').val('');
           $('#search-state').show().prop('name', 'q');
        }
        else {
            $('#search-state').hide().prop('name', '').val('');
            $('#search-term').show().prop('name', 'q');
        }
    }

    // call change input to determine which text input to show/hide at page load and on change
    changeInput();

    $('#select-category').change(changeInput);

    // alpha navigation functionality
    // show only items for the clicked letter
    $(".alpha-nav a").click(function() {
        var filter = $(this).data("filter");

        // make the clicked letter have active color
        $(".alpha-nav>li.selected").removeClass("selected");
        $(this).parent().addClass("selected");


        if(filter === "all") {
            $(".letter").show();    // show all results
        }
        else {
            $(".letter").hide();    // hide all
            $("." + filter).show(); // show the one set of results
        }
        return false;
    });

    // grey out letters without matches
    $(".alpha-nav a").each(function() {
        var filter = $(this).data("filter");
        if (filter != "all") {
            var count = $("." + filter).length;
            if (count == 0) {
                $(this).addClass("alpha-disabled");
            }
        }
    });

    // attach onclick handlers for more/less text in accordions
    $(".cell .more").click(function () {
        $(this).prev(".text").addClass("expanded");
        $(this).toggle();
        $(this).next(".less").toggle();
    });

    $(".cell .less").click(function () {
        $(this).prevAll(".text").removeClass("expanded");
        $(this).toggle();
        $(this).prev(".more").toggle();
    });

    // functionality to support accordion expand/collapse of divs for large bodies of text
    function accordionActivate(event, ui) {
        $(ui.newPanel).find('.cell').each(function () {
            var cell = this;
            var text = $(cell).find(".text");
            var more = $(cell).find(".more");
            var less = $(cell).find(".less");

            // correct for resizing
            if ($(text).height() < 55) {
                //$(more).hide();
                $(text).removeClass("text");
            }
            else {
                if(!$(less).is(":visible")) {
                    $(more).show();
                }
            }
        });
    }

    // remain on tab when page changes
    $('.fda-pagination li a').click(function(e){
        var newdiv = window.location.hash;
        var href = $(this).attr('href');
        e.preventDefault();
        window.location = $(this).attr('href') + newdiv;
    });

    // display appropriate tab
    $('.ui-tabs-nav li a').click(function(e){
        e.preventDefault();
        var newdiv = $(this).attr('href');
        window.location.hash = newdiv;
        $('.fda-tabs-interface li').removeClass('active');
        $(this).parent('li').addClass('active');
        $('.contents div').hide();
        $(newdiv).show()
    });
});
