{
    let floating=document.querySelector('.floating_menu');
    let others=document.querySelector('.others');
    floating.addEventListener("click",function(){
        others.classList.toggle("active");
        floating.classList.toggle("active");
        
    });
    
}