<script>
    function submitLanguageForm() {
        // Soumet le formulaire
        document.getElementById('language-form').submit();
    }

    // Écoute les changements de langue
    document.getElementById('language-form').onsubmit = function() {
        // Cache le sélecteur et montre le bouton
        document.getElementById('language-selector').style.display = 'none';
        document.getElementById('language-button').style.display = 'block';
    };
</script>