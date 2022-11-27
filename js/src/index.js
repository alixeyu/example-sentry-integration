import * as Sentry from "@sentry/browser"
import { BrowserTracing } from "@sentry/tracing"

Sentry.init({
    dsn: "https://1ea7d8916e864dc0acf1ac85d95c5625@o366150.ingest.sentry.io/4504229353422848",
    integrations: [new BrowserTracing()]
})

UndefinedFunction();
