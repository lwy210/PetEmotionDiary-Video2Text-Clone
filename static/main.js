var diary_data = {

};

function getDiarys(callback) {
    $.ajax({
        type:'GET',
        // url : '{% url "diary:get_diarys"  %}',
        url : "http://127.0.0.1:8000/diary/get_diarys/",
        success: function(response){
            diary_data = response
            if (typeof callback === "function") { // callback이 함수인 경우에만 호출
                callback();
            }
        },
        error: function(response){
            alert("An Error Occured");
        },
    });
}
// 그 다음부터는 지정된 시간 간격으로 실행
setInterval(function(){
    getDiarys(); // 콜백 없이 호출
}, 1000);


(function($) {

	"use strict";

	// Setup the calendar with the current date
$(document).ready(function(){
    getDiarys(function() {
        var date = new Date();
        var today = date.getDate();
        // Set click handlers for DOM elements
        $(".right-button").click({date: date}, next_year);
        $(".left-button").click({date: date}, prev_year);
        $(".month").click({date: date}, month_click);
        // Set current month as active
        $(".months-row").children().eq(date.getMonth()).addClass("active-month");
        init_calendar(date);
        // var events = check_events(today, date.getMonth()+1, date.getFullYear());
        var diarys = check_diarys(today, date.getMonth()+1, date.getFullYear());
    });
});

// Initialize the calendar by appending the HTML dates
function init_calendar(date) {
    $(".tbody").empty();
    $(".events-container").empty();
    var calendar_days = $(".tbody");
    var month = date.getMonth();
    var year = date.getFullYear();
    var day_count = days_in_month(month, year);
    var row = $("<tr class='table-row'></tr>");
    var today = date.getDate();
    // Set date to 1 to find the first day of the month
    date.setDate(1);
    var first_day = date.getDay();
    // 35+firstDay is the number of date elements to be added to the dates table
    // 35 is from (7 days in a week) * (up to 5 rows of dates in a month)
    for(var i=0; i<35+first_day; i++) {
        // Since some of the elements will be blank, 
        // need to calculate actual date from index
        var day = i-first_day+1;
        // If it is a sunday, make a new row
        if(i%7===0) {
            calendar_days.append(row);
            row = $("<tr class='table-row'></tr>");
        }
        // if current index isn't a day in this month, make it blank
        if(i < first_day || day > day_count) {
            var curr_date = $("<td class='table-date nil'>"+"</td>");
            row.append(curr_date);
        }   
        else {
            var curr_date = $("<td class='table-date'>"+day+"</td>");
            // var events = check_events(day, month+1, year);
            var diarys = check_diarys(day, month+1, year);
            // active된 날짜가 없으면 오늘 날짜로 activate
            if(today===day && $(".active-date").length===0) {
                curr_date.addClass("active-date");
                // 오늘 날짜 active 됐으니 오른쪽 칸에 보여주기
                 
                // setInterval(function() {
                    show_events(months[month], day, diarys);
                // }, 1000);
            }
            if(diarys.length!==0) {
                curr_date.addClass("diary-date");
            }
            // Set onClick handler for clicking a date
            curr_date.click({month: months[month], day:day, diarys: diarys}, date_click);
            row.append(curr_date);
        }
    }
    // Append the last row and set the current year
    calendar_days.append(row);
    $(".year").text(year);
}

// Get the number of days in a given month/year
function days_in_month(month, year) {
    var monthStart = new Date(year, month, 1);
    var monthEnd = new Date(year, month + 1, 1);
    return (monthEnd - monthStart) / (1000 * 60 * 60 * 24);    
}

// Event handler for when a date is clicked
function date_click(event) {
    $(".events-container").show(250);
    $("#dialog").hide(250);
    $(".active-date").removeClass("active-date");
    $(this).addClass("active-date");
    show_events(event.data.month, event.data.day, event.data.diarys); //
};

// Event handler for when a month is clicked
function month_click(event) {
    $(".events-container").show(250);
    $("#dialog").hide(250);
    var date = event.data.date;
    $(".active-month").removeClass("active-month");
    $(this).addClass("active-month");
    var new_month = $(".month").index(this);
    date.setMonth(new_month);
    init_calendar(date);
}

// Event handler for when the year right-button is clicked
function next_year(event) {
    $("#dialog").hide(250);
    var date = event.data.date;
    var new_year = date.getFullYear()+1;
    $("year").html(new_year);
    date.setFullYear(new_year);
    init_calendar(date);
}

// Event handler for when the year left-button is clicked
function prev_year(event) {
    $("#dialog").hide(250);
    var date = event.data.date;
    var new_year = date.getFullYear()-1;
    $("year").html(new_year);
    date.setFullYear(new_year);
    init_calendar(date);
}


function get_bookmark_state(diary_id) {

}


// Display all events of the selected date in card views
function show_events(month, day, diarys) {
    // Clear the dates container //
    $(".events-container").empty();
    $(".events-container").show(250);
    // If there are no events for this date, notify the user

    if(diarys.length===0) {
        // // diary 없을때 보여주는 거
        var diary_card = $("<div class='diary-card'></div>");
        var diary_name = $("<div class='diary-name'>There are no diarys planned for "+month+" "+day+".</div>");
        $(diary_card).css({ "border-left": "10px solid #FF1744" });
        $(diary_card).append(diary_name);

        // append
        $(".events-container").append(diary_card);
    }
    else {
        // diary 보여주기
        for(var i=0; i<diarys.length; i++) {
            var id = diarys[i].id
            // var keywords
            var diary_card = $("<div class='diary-card'></div>");
            (function(id, diary_card) {
            $.ajax({
                type:'GET',
                url : "http://127.0.0.1:8000/diary/get_diary_info/"+id.toString()+"/",
                success: function(response){
                    var diary_title = $('<a href="/diary/' + id + '/"><h3>' + response["title"] + '</h3></a>');
                    var keywords_div = "";
                    var keywords = response["keywords"];
                    // bookmark = response["bookmark"];
                    for(var j = 0; j < keywords.length; j++) {
                        keywords_div += "<div>#" + keywords[j] + "</div>";
                    }
                    var diary_element = $("<div></div>");
                    diary_element.append(diary_title);
                    diary_element.append(keywords_div);

                     // Creating bookmark form dynamically using JavaScript
                    var bookmarkForm = $("<form></form>");
                    bookmarkForm.attr("action", diaryBookmarkUrl.replace('0', id.toString()));
                    bookmarkForm.attr("method", "POST");

                     // Creating csrf input field
                    var csrfInput = $("<input></input>");
                    csrfInput.attr("type", "hidden");
                    csrfInput.attr("name", "csrfmiddlewaretoken");
                    csrfInput.attr("value", csrftoken);  // The csrftoken variable that you've obtained above

                    var submitButton = $("<input></input>");
                    submitButton.attr("type", "submit");
                    submitButton.attr("value", "Bookmark");
                    submitButton.addClass("btn btn-sm btn-outline-danger");

                    bookmarkForm.append(csrfInput);  // Append csrf input to form
                    bookmarkForm.append(submitButton);
                    diary_element.append(bookmarkForm);

                    // 북마크 상태
                    var bookmarkState = $('<div>' + response["bookmark"] + '</div>');
                    diary_element.append(bookmarkState);

                    $(diary_card).append(diary_element);
                    $(".events-container").append(diary_card);

                     // AJAX bookmark form submission
                    bookmarkForm.submit(function(e) {
                        e.preventDefault();  // Prevent the form from being submitted normally
                        $.ajax({
                            type: "POST",
                            url: bookmarkForm.attr('action'),
                            data: bookmarkForm.serialize(),
                            success: function(response) {
                                show_events(month, day, diarys)
                                bookmarkState.text(response["bookmark"]);
                            },
                            error: function(response) {
                                alert('An error occurred while bookmarking');
                            }
                        });
                    });
                },
                error: function(response){
                    alert("An Error Occured");
                },
            });
        })(id, diary_card);
        }
    }
}


function check_diarys(day, month, year) {
    var diarys = []
    for(var i=0; i<diary_data["diarys"].length; i++) {
        var diary = diary_data["diarys"][i];
        var date = new Date(diary["day"]);
        if(date.getDate()===day &&
        date.getMonth()+1===month &&
        date.getFullYear()===year) {
            diarys.push(diary);
        }
    }
    diarys.sort(function(a, b) {
        var dateA = new Date(a["updated_time"]), dateB = new Date(b["updated_time"]);
        return dateB - dateA;
    });
    return diarys
}

const months = [ 
    "January", 
    "February", 
    "March", 
    "April", 
    "May", 
    "June", 
    "July", 
    "August", 
    "September", 
    "October", 
    "November", 
    "December" 
];

})(jQuery);