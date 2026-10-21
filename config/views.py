from django.db import connection
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status


class HealthCheckView(APIView):
    permission_classes = [AllowAny]
    throttle_classes = []

    def get(self, request):
        health_status = {
            "status": "ok",
            "database": False,
            "redis": False,
        }

        # Check PostgreSQL
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                health_status["database"] = True
        except Exception as exc:
            health_status["status"] = "degraded"
            health_status["database_error"] = str(exc)

        # Check Redis Cache
        try:
            cache.set("health_check_ping", "pong", timeout=10)
            if cache.get("health_check_ping") == "pong":
                health_status["redis"] = True
        except Exception as exc:
            health_status["status"] = "degraded"
            health_status["redis_error"] = str(exc)

        http_status = (
            status.HTTP_200_OK
            if health_status["status"] == "ok"
            else status.HTTP_503_SERVICE_UNAVAILABLE
        )
        return Response(health_status, status=http_status)
