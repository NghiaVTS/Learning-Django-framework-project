//write function
function addActive(item) {
    item.classList.add('active');
};

function removeActive(item) {
    item.classList.remove('active');
};

function toggleActive(item) {
    item.classList.toggle('active');
};

//back to top
function btt() {
    let btn = document.querySelector('.footer .btt-btn');
    if (document.contains(btn) == true) {
        btn.addEventListener('click', function () {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        })
    }
}

//nav menu toggle
function navMenu() {
    let nav = document.querySelector('.nav'),
        btnMenu = document.querySelector('.header .header__btnmenu');
    if (document.contains(nav) == true && document.contains(btnMenu) == true) {
        btnMenu.addEventListener('click', function () {
            toggleActive(this);
            toggleActive(nav);
        });

        function hideNav() {
            removeActive(btnMenu);
            removeActive(nav);
        }

        window.addEventListener('resize', function () {
            let wWindow = window.innerWidth;
            if (wWindow > 992) {
                hideNav();
            }
        })
    }
}

//video pop up
function videoPopUp() {
    let box = document.querySelector('.videobox'),
        video = document.querySelectorAll('.video'),
        close = document.querySelector('.close-btn');

    video.forEach(function (item) {
        item.addEventListener('click', function (event) {
            let iframe = document.querySelector('.iframe')
            data = this.dataset.src;
            iframe.setAttribute('src', data);
            addActive(box)
        })
    });

    function unactive() {
        removeActive(box)
    }
    close.addEventListener('click', function () {
        unactive()
    });
}

// //test flikity
// function slider() {
//     //call flkty
//     var heroBanner = document.querySelector('.scherobanner');
//     if (document.contains(heroBanner) == true) {
//         var flkty = new Flickity(
//             heroBanner,
//             {
//                 draggable: false,
//                 freeScroll: false,
//                 contain: true,
//                 prevNextButtons: false,
//                 pageDots: false,
//                 wrapAround: true
//             }
//         );
//     }
//     // //set variables
//     // var number = document.querySelector('.scbanner__stay .number');

//     // //set number for page
//     // flkty.on('change', function (index) {
//     //     number.innerHTML = '0' + (index + 1);
//     // });

//     // previous
//     // var previousButton = document.getElementById('previous');
//     // previousButton.addEventListener('click', function () {
//     //     flkty.previous(true);
//     // });
//     // //next
//     // var nextButton = document.getElementById('next');
//     // nextButton.addEventListener('click', function () {
//     //     flkty.next(true);
//     // });

// }

//slider gallery
function imgSlide() {
    //khoi tao
    var img = document.querySelector('.scos__sliders');
    if (document.contains(img) == true) {
        var flkty = new Flickity(
            img,
            {
                freeScroll: false,
                prevNextButtons: true,
                wrapAround: true,
                lazyLoad: 3,
                draggable: false,
                autoPlay: 2000,
                pauseAutoPlayOnHover: true
            }
        );
    }
}

//gallery
function galleryShow() {
    Fancybox.bind('[data-fancybox]', {
        caption: function (fancybox, carousel, slide) {
            return (
                `${slide.index + 1} / ${carousel.slides.length} <br />` + slide.caption
            );
        },
    });
}


window.addEventListener('load', function () {
    btt(); navMenu(); imgSlide(); videoPopUp(); galleryShow();
    //    slider();
})