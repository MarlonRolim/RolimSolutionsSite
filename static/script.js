(function () {
    var menu = document.getElementById('menu'); // colocar em cache
    window.addEventListener('scroll', function () {
        if (window.scrollY > 10) menu.classList.remove('cabecalho'); // > 0 ou outro valor desejado
        else menu.classList.remove('cabecalho');
    });
})();