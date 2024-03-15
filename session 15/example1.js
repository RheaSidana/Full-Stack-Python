// function myBtnFn(){
//     document.getElementsByTagName("p")[0].innerText = "I am modified";
// }

// window.addEventListener("load", function() {
//     document.getElementsByTagName("p")[0].addEventListener("click", function modifyByOurCustomText(){
//         document.getElementsByTagName("p")[0].innerText = "My modified paragraph.";
//         document.body.removeChild(document.getElementsByTagName("p")[2]);
//     });
// });

window.onload = function(){
    // document.getElementsByTagName("p")[0].addEventListener("click", function modifyByOurCustomText(){
    //     document.getElementsByTagName("p")[0].innerText = "My modified paragraph.";
    //     document.body.removeChild(document.getElementsByTagName("p")[2]);
    // });

    document.write("<h1>I am text in h1 tag</h1>I am text in p tag");
    document.write("<p>I am para through js</p>")
}