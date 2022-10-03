package a.gleb.passwordgeneratorlab2

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material.Button
import androidx.compose.material.MaterialTheme
import androidx.compose.material.OutlinedTextField
import androidx.compose.material.Text
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.application
import androidx.compose.ui.window.rememberWindowState
import mu.KotlinLogging
import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import kotlin.math.pow
import kotlin.random.Random

var logger = KotlinLogging.logger { }
private val ASCII_PAIR_UPPER_CASE: Pair<Int, Int> = Pair(65, 90)
private val ASCII_PAIR_LOWER_CASE: Pair<Int, Int> = Pair(97, 122)
private val SYMBOLS = listOf('!', '"', '#', '$', '%', '&', '’', '(', ')', '*')

/**
 * @author Abakshin-Bavitsky.G.G
 * БПИз-18-01
 */
@SpringBootApplication
class PasswordGeneratorLab2Application

fun main(args: Array<String>) = application {
    runApplication<PasswordGeneratorLab2Application>(*args)
    Window(
        onCloseRequest = ::exitApplication,
        title = "Password generator",
        state = rememberWindowState(width = 300.dp, height = 300.dp),
        resizable = false
    ) {
        MaterialTheme {
            val message = remember { mutableStateOf("") }
            var generatePassword = remember { mutableStateOf("") }
            Column(Modifier.fillMaxSize(), Arrangement.spacedBy(5.dp)) {
                OutlinedTextField(
                    message.value,
                    onValueChange = { message.value = it },
                    textStyle = TextStyle(fontSize = 30.sp),
                )
                Button(modifier = Modifier.align(Alignment.CenterHorizontally),
                    onClick = {
                        generatePassword.value = generatePassword(message.value)
                        message.value = ""
                        logger.info { "Program generate password: ${generatePassword.value}" }
                    }) {
                    Text("Generate password")
                }
                Text(
                    modifier = Modifier.align(Alignment.CenterHorizontally),
                    text = generatePassword.value,
                    fontWeight = FontWeight.Bold
                )
            }
        }
    }
}


/**
 * @author Abakshin-Bavitsky G.G
 * БПИз-18-01
 */
private fun generatePassword(userCredential: String): String {
    val passwordArray = mutableListOf<Char>()
    /* random digit 0 .. 9 */
    val randomDigit = Random.nextInt(0, 9)
    /* sqr(N) mod 10 */
    val userCredMod = userCredential.length.toDouble().pow(2) % 10
    /* random symbol from array */
    val fourthSymbolOfPassword = SYMBOLS[Random.nextInt(0, SYMBOLS.size - 1)]

    /* add symbols to array of chars */
    passwordArray.add(Char(Random.nextInt(ASCII_PAIR_UPPER_CASE.first, ASCII_PAIR_UPPER_CASE.second)))
    passwordArray.add(Char(Random.nextInt(ASCII_PAIR_UPPER_CASE.first, ASCII_PAIR_UPPER_CASE.second)))
    passwordArray.add(userCredMod.toInt().digitToChar())
    passwordArray.add(randomDigit.digitToChar())
    passwordArray.add(fourthSymbolOfPassword)
    passwordArray.add(Char(Random.nextInt(ASCII_PAIR_LOWER_CASE.first, ASCII_PAIR_LOWER_CASE.second)))

    return String(passwordArray.toCharArray())
}