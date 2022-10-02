package a.gleb.passwordstrengthlab.configuration

import a.gleb.passwordstrengthlab.configuration.properties.PasswordStrengthProperties
import org.springframework.boot.context.properties.EnableConfigurationProperties
import org.springframework.context.annotation.Configuration

@EnableConfigurationProperties(PasswordStrengthProperties::class)
@Configuration
class PasswordStrengthConfig {
}