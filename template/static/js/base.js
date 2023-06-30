$(document).ready(() => {
    $("#back-to-top").click(() => {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    })
})

function darktheme() {
    $('body').toggleClass('dark-theme');
}
// gsap.set('.main', { background: '#fff', height: '120%' })
// gsap.timeline({ scrollTrigger: { trigger: '.scrollDist', start: 'top top', end: 'bottom bottom', scrub: 2 } })
//     .fromTo('.sky', { y: 100 }, { y: -650 }, 0)
//     .fromTo('.cloud1', { y: 50 }, { y: -750 }, 0)
//     .fromTo('.cloud2', { y: -100 }, { y: -750 }, 0)
//     .fromTo('.cloud3', { y: -50 }, { y: -750 }, 0)
//     .fromTo('.mountBg', { y: -10 }, { y: -100 }, 0)
//     .fromTo('.mountMg', { y: -20 }, { y: -250 }, 0)
//     .fromTo('.mountFg', { y: -40 }, { y: -500 }, 0)
