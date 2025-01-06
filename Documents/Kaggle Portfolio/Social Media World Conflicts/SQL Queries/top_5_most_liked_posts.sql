SELECT TOP 5 
    platform, 
    text, 
    likes, 
    views, 
    uploader, 
    conflict
FROM EngagementData
ORDER BY likes DESC;
