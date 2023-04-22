
$(document).ready(function() {
    $('.followers').click(function() {
        $('.followers-article').toggleClass('active');
    });
    $('.close-followers').click(function() {
      $('.followers-article').toggleClass('active');
    })

       $('.following').click(function() {
        $('.following-article ').toggleClass('active');
    });
    $('.close-following').click(function() {
      $('.following-article').toggleClass('active');
    })
    $('.error-close').click(function() {
      $('.error').hide();
    })

})
