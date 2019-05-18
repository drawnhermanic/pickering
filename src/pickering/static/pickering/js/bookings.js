var bookingDateRange = [];

$(document).ready(function() {

    bookingFormEventHandlers();
    bookingDatePickerInit();

})

function bookingFormEventHandlers() {

    //event handlers go here
    //$(document).on('click tap', '.booking-dates__input', function() { bookingDatesEventHandler(); });

}

function bookingDatePickerInit() {

    $('.booking-dates__datepicker').datepicker({
        dateFormat: "yy-mm-dd", 
        numberOfMonths: 3,
        onSelect: function (dateText, inst) {
            setDateRange(dateText);
        },
        beforeShowDay: function (date) {
            return getDateHighlightState(date);
        }
    });

}

function setDateRange(dateText, inst) {
    var date = new Date(dateText);
    
    if (bookingDateRange.map(Number).indexOf(+date) > -1) {
        bookingDateRange.splice( bookingDateRange.map(Number).indexOf(+date), 1 );
    } else {
        bookingDateRange.push(date);
    }

    setBookingStartAndEndDates();
}

function setBookingStartAndEndDates() {

    var bookingDateFrom = new Date(Math.min.apply(null,bookingDateRange));
    var bookingDateTo = new Date(Math.max.apply(null,bookingDateRange));
    
    $('#id_date_from').val(bookingDateFrom.toLocaleDateString('en-GB'));
    $('#id_date_to').val(bookingDateTo.toLocaleDateString('en-GB'));

}

function getDateHighlightState(date) {

    var matchingDates = jQuery.grep(bookingDateRange, function( n, i ) {
        return ( bookingDayMatch(date, n) );
      });

    if (matchingDates.length) {
        // Enable date so it can be deselected. Set style to be highlighted
        return [true, "ui-state-highlight"];
    }
    // Dates not in the array are left enabled, but with no extra style
    return [true, ""];

}

function bookingDayMatch(d1, d2) {
    return d1.getFullYear() === d2.getFullYear() &&
      d1.getMonth() === d2.getMonth() &&
      d1.getDate() === d2.getDate();
  }