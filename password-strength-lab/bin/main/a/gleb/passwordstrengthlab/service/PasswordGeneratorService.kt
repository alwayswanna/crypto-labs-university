package a.gleb.passwordstrengthlab.service

import a.gleb.passwordstrengthlab.configuration.properties.PasswordStrengthProperties
import mu.KotlinLogging
import org.springframework.boot.CommandLineRunner
import org.springframework.stereotype.Service
import java.math.BigInteger
import java.util.concurrent.TimeUnit
import kotlin.math.ceil
import kotlin.math.log
import kotlin.random.Random

/**
 * @author Abakshin-Bavitsky.G.G
 */


/**
 * Seconds in one day.
 */
private const val DAY_TO_SECOND = 86400

/**
 * ASCII - code for password.
 */
private val ASCII_PAIR: Pair<Int, Int> = Pair(65, 122)

var logger = KotlinLogging.logger { }

@Service
class PasswordGeneratorService(val passwordStrengthProperties: PasswordStrengthProperties) : CommandLineRunner {

    override fun run(vararg args: String?) {
        val password = generatePassword()
        logger.info { "Program generate password: $password" }
    }

    fun generatePassword(): String {
        val lengthOfDictionary = ASCII_PAIR.second - ASCII_PAIR.first

        val lengthOfPassword =
            ceil((log(getLowerBound().toDouble(), 2.0) / log(lengthOfDictionary.toDouble(), 2.0)))
                .toInt()

        logger.info { "Length of password: $lengthOfPassword" }

        val password = mutableListOf<Char>()
        for (i in 1..lengthOfPassword) {
            password.add(Char(Random.nextInt(ASCII_PAIR.first, ASCII_PAIR.second)))
            i.inc()
        }

        return String(password.toCharArray())
    }

    /**
     * Return lower bound for password generator.
     */
    private fun getLowerBound(): BigInteger {
        logger.info { "Start find lower bound for password" }
        val lowerBound = with(passwordStrengthProperties) {
            /* convert all values to second */
            val passwordExpiredPeriodInSeconds = passwordExpiredPeriodDays.toDouble() * DAY_TO_SECOND
            val attemptsPerSecond = convertAttemptsToSeconds(countPassPerUnitTime, unitTime)
            ceil((passwordExpiredPeriodInSeconds * attemptsPerSecond) / passwordGuessingProbability)
                .toBigDecimal()
                .toBigInteger()
        }
        logger.info { "End find lower bound for password, value: $lowerBound" }
        return lowerBound
    }

    /**
     * Convert attempts to [TimeUnit] in attempts to second
     */
    private fun convertAttemptsToSeconds(attempt: Int, timeUnit: TimeUnit): Double {
        when (timeUnit) {
            TimeUnit.SECONDS -> return attempt.toDouble()
            TimeUnit.MINUTES -> return attempt.toDouble() / 60
            TimeUnit.HOURS -> return attempt.toDouble() / 3600
            TimeUnit.DAYS -> return attempt.toDouble() / 86400
        }
        throw IllegalStateException("Incorrect timeUnit value.")
    }
}
