document.addEventListener('DOMContentLoaded', function() {
    const tokenInput = document.getElementById('token-form');
    
    function generateToken() {
        const letters = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z'
        ];
        let result = "";
        for (let i = 0; i < 16; i++) {
            if (i % 4 === 0 && i !== 0) {
                result += "-";
            }
            result += letters[Math.floor(Math.random() * letters.length)];
        }
        return result;
    }

    function updateTokenField() {
        const token = generateToken();
        tokenInput.value = token;
    }

    updateTokenField();

});
