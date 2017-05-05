//初始化fileinput控件（第一次初始化）
function initFileInput(ctrlName, uploadUrl) {
    var control = $('#' + ctrlName);
    control.fileinput({
        language: 'zh', //设置语言
        uploadUrl: uploadUrl, //上传的地址
        // showUpload: false, //是否显示上传按钮
        // showCaption: false,//是否显示标题
        // browseClass: "btn btn-primary", //按钮样式
        previewFileIcon: "<i class='glyphicon glyphicon-king'></i>",
        maxFileCount: 9,
        //allowedFileTypes:['image'], //先于allowedFileExtensions验证
        allowedFileExtensions:['jpg', 'png', 'gif'],
        previewFileType:['jpg','png','gif'],
        previewClass: "bg-warning",
        dropZoneEnabled:false
    });
}


//初始化fileinput控件（第一次初始化）
initFileInput("file-Portrait", "/User/EditPortrait");