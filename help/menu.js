
      
    const botones = document.getElementsByClassName('margin-right-small large-up-margin-right-medium').item(0);
    const ranking = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(0);
    const collections = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(1);
    const computer = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(2)
    const health = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(3)
    const math = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(4)
    const business = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(5)
    const humanities = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(6)
    const engin = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(7)
    const science = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(8)
    const education = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(9)
    const social = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(10)
    const art = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(11)
    const data = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(12)
    const programming = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(13)
    const personal = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(14)
    const information = document.getElementsByClassName('main-nav-dropdown__item-control color-charcoal').item(15)

    const rightSide = document.getElementsByClassName('main-nav-dropdown__subsections').item(0)

    var desactivate = true;


    const navMenu = document.getElementsByClassName('main-nav-dropdown__section').item(0);
    const secondMenu = document.getElementsByClassName('list-no-style').item(1)

    let z = false;

     function activateNav() {
        var elemento = document.getElementsByClassName('main-nav-dropdown js-main-nav-dropdown');
        console.log(elemento)
        var nav = elemento.item(0);
        nav.classList.add('is-open');

        nav.style.display = "grid"

        var html = document.getElementsByClassName('sticky-footer') 
        html.item(0).className = 'sticky-footer nav-open'

        var elemento2 = document.getElementsByClassName('width-100 height-100 fixed top left animate-fade-hidden');
        elemento2.item(0).className = 'width-100 height-100 fixed top left'
      };


      function deactivateNav() {
        var elemento = document.getElementsByClassName('main-nav-dropdown js-main-nav-dropdown is-open');
        var nav = elemento.item(0);
        nav.classList.remove('is-open');
        nav.style.display = "none";
        nav.style.top = "";
        nav.style.left = ""

        var html = document.getElementsByClassName('sticky-footer nav-open') 
        html.item(0).className = 'sticky-footer'

        var elemento2 = document.getElementsByClassName('width-100 height-100 fixed top left');
        elemento2.item(0).className = 'width-100 height-100 fixed top left animate-fade-hidden'

    
      };


    function activateElement(number){

        try{
    
            var menuRanking = document.getElementsByClassName('main-nav-dropdown__subsection js-main-nav-subsection').item(number)
            menuRanking.classList.add('is-selected')
            menuRanking.removeAttribute('hidden')
    
    
        }catch{
            console.log('Saltó un elemento');
        }

    }
      
      
      
      function deactiativateElements(listOfNumbers){

        for(let elemento of listOfNumbers){
            try{
    
                var menuRanking = document.getElementsByClassName('main-nav-dropdown__subsection js-main-nav-subsection').item(elemento)
                    menuRanking.classList.remove('is-selected')
                    menuRanking.setAttribute('hidden', '')
        
        
            }catch{
                console.log('Saltó un elemento');
            }
        }
      }



      function navMenuAct(){

        var elemento = document.getElementsByClassName('main-nav-dropdown js-main-nav-dropdown is-open');
        var nav = elemento.item(0);
        nav.classList.add('has-visibile-subsection');

      }


botones.addEventListener('mousemove', function() {
    if(z === false){
        activateNav();
        z = true
        console.log('Entró al activador')
    }
});

botones.addEventListener('mouseleave', function() {
    if(z === true && desactivate === true){
        deactivateNav();
        z = false
        console.log('Entró al desactivador')
    }
    
});

navMenu.addEventListener('mousemove', function() {
    navMenuAct()
});



ranking.addEventListener('mousemove', function() {

    let i = 0
    activateElement(i);
    let numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];
    deactiativateElements(numbers);
});



collections.addEventListener('mousemove', function() {

    let i = 1
    activateElement(i);
    let numbers = [0,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    deactiativateElements(numbers);

});



computer.addEventListener('mousemove', function() {

    let i = 2
    activateElement(i);
    let numbers = [0,1,3,4,5,6,7,8,9,10,11,12,13,14,15]
    deactiativateElements(numbers);
});


health.addEventListener('mousemove', function() {

    let i = 3
    activateElement(i);
    let numbers = [0,1,2,4,5,6,7,8,9,10,11,12,13,14,15]
    deactiativateElements(numbers);
});



math.addEventListener('mousemove', function() {
    let i = 4
    activateElement(i);
    let numbers = [0,1,2,3,5,6,7,8,9,10,11,12,13,14,15]
    deactiativateElements(numbers);
});


business.addEventListener('mousemove', function() {

    let i = 5
    activateElement(i);
    let numbers = [0,1,2,3,4,6,7,8,9,10,11,12,13,14,15]
    deactiativateElements(numbers);
});


humanities.addEventListener('mousemove', function() {
    let i = 6
    activateElement(i);
    let numbers = [0,1,2,3,4,5,7,8,9,10,11,12,13,14,15]
    deactiativateElements(numbers);
});


engin.addEventListener('mousemove', function() {
    let i = 7
    activateElement(i);
    let numbers = [0,1,2,3,4,5,6,8,9,10,11,12,13,14,15]
    deactiativateElements(numbers);
});


science.addEventListener('mousemove', function() {

    let i = 8
    activateElement(i);
    let numbers = [0,1,2,3,4,5,6,7,9,10,11,12,13,14,15]
    deactiativateElements(numbers);
});


education.addEventListener('mousemove', function() {

    let i = 9
    activateElement(i);
    let numbers = [0,1,2,3,4,5,6,7,8,10,11,12,13,14,15]
    deactiativateElements(numbers);
});

social.addEventListener('mousemove', function() {
    let i = 10
    activateElement(i);
    let numbers = [0,1,2,3,4,5,6,7,8,9,11,12,13,14,15]
    deactiativateElements(numbers);
});


art.addEventListener('mousemove', function() {
    let i = 11
    activateElement(i);
    let numbers = [0,1,2,3,4,5,6,7,8,9,10,12,13,14,15]
    deactiativateElements(numbers);
});


data.addEventListener('mousemove', function() {
    let i = 12
    activateElement(i);
    let numbers = [0,1,2,3,4,5,6,7,8,9,10,11,13,14,15]
    deactiativateElements(numbers);
});


programming.addEventListener('mousemove', function() {

    let i = 13
    activateElement(i);
    let numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,14,15]
    deactiativateElements(numbers);
});

personal.addEventListener('mousemove', function() {

    let i = 14
    activateElement(i);
    let numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15]
    deactiativateElements(numbers);
});

information.addEventListener('mousemove', function() {
    
    let i = 15
    activateElement(i);
    let numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    deactiativateElements(numbers);
});


secondMenu.addEventListener('mousemove', function() {
    navMenuAct()
});