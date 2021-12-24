var socket = io.connect('http://'+document.domain+':'+location.port);

socket.on('connect',function(){
    socket.emit('evt',{
        data: 'User Connected'
    })
    var form = $('form').on('submit', function(e){
        e.preventDefault();
        let username = $('input.username').val();
        let msg = $('input.msg').val();
        socket.emit('evt',{
            user_name: username,
            message: msg
        })
        $('input.msg').val('').focus();
    });
});

socket.on('response_return', function (msg) {
    console.log(msg);
    if(typeof msg.user_name !== 'undefined'){
        $('h3').remove();
        $('msg_content').append('<div><b>'+msg.user_name+'<\b> '+msg.msg+'</div>');
    }
})