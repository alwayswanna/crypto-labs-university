package a.gleb.passwordstrengthlab.configuration.properties

import org.springframework.boot.context.properties.ConfigurationProperties
import org.springframework.boot.context.properties.ConstructorBinding
import java.util.concurrent.TimeUnit

@ConfigurationProperties("app-config")
@ConstructorBinding
data class PasswordStrengthProperties(
    /**
     * Password expired period in days.
     */
    val passwordExpiredPeriodDays: Int,
    /**
     * Password per unit (bruteforce).
     */
    val countPassPerUnitTime: Int,
    /**
     * Time unit (bruteforce).
     */
    val unitTime: TimeUnit,
    /**
     * Max password guessing probability (bruteforce).
     */
    val passwordGuessingProbability: Double
)